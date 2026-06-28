# Syllabus Extractor — Design Document

## Architecture Overview

The application follows a simple pipeline with a source-dispatch step that routes a URL to the correct downloader and parser based on its host:

```
                          ┌─ udemy.com   → [Udemy Downloader]   → [Udemy Parser]
[Web UI] → [Source Router]─┤                                                      ├→ [Markdown Generator]
                          └─ w3schools.com → [W3Schools Downloader] → [W3Schools Parser]
```

Both parsers emit the **same intermediate dict** (`title`, `objectives`, `syllabus`), so the markdown generator is shared and source-agnostic. W3Schools yields an empty `objectives` list and `description: None` on every sub-section.

All layers are pure Python. The web UI is served locally via a lightweight framework (Flask). No database is used; state lives only in memory during a single extraction run.

---

## Module Breakdown

### `app.py` — Web Server / Entry Point
- Starts the Flask development server.
- Serves the single-page UI.
- Exposes a POST endpoint (`/extract`) that accepts a Udemy **or** W3Schools URL, routes it via the source router, and returns the path to the generated markdown file.

### Source Router (URL → source)
- A small dispatch helper (lives in `app.py` or a dedicated `source.py`) inspects the URL host.
- `udemy.com` → Udemy downloader + Udemy parser.
- `w3schools.com` → W3Schools downloader + W3Schools parser.
- Unknown host → validation error surfaced to the UI.

### `downloader.py` — Udemy HTML Downloader
- Accepts a Udemy course URL.
- Downloads the fully JS-rendered HTML using Playwright, expanding all collapsed curriculum sections first.
- Saves the raw HTML to `HTML Files/<course-slug>.html`.
- Returns the local file path.

### `w3schools_downloader.py` — W3Schools HTML Downloader
- Accepts a W3Schools tutorial URL.
- Downloads the **static** HTML with a plain request (no JS rendering, no section expansion).
- Derives a slug from the URL path (e.g. `js/default.asp` → `js-default`) and saves to `HTML Files/<slug>.html`.
- Returns the local file path.

### `parser.py` — Udemy HTML Parser
- Accepts a path to a local HTML file.
- Uses BeautifulSoup to extract:
  - **Course objectives** — list of strings.
  - **Syllabus** — 3-dimensional structure: `list[section]`, where each section contains a title and a `list[sub_section]`, where each sub-section contains a title and an optional description string.
- Returns a structured Python dict:
  ```python
  {
      "objectives": ["...", "..."],
      "syllabus": [
          {
              "title": "Section Title",
              "sub_sections": [
                  {"title": "Lecture Title", "description": "Optional text or None"},
                  ...
              ]
          },
          ...
      ]
  }
  ```

### `w3schools_parser.py` — W3Schools HTML Parser
- Accepts a path to a local HTML file.
- Uses BeautifulSoup to walk the left-menu container (`id="leftmenuinnerinner"`):
  - **title** — the `<h2 class="left">` subject name (e.g. "JS Tutorial").
  - **syllabus** — iterate the direct children of the menu container in document order. Each top-level `<a target="_top">` opens a new section; if the next sibling is a `<div class="tut_overview">`, its inner `<a target="_top">` elements become that section's sub-sections. A section `<a>` with no following `tut_overview` is a standalone section with an empty `sub_sections` list.
- Returns the **same** dict shape as `parser.py`, with `objectives: []` and every sub-section's `description: None`:
  ```python
  {
      "title": "JS Tutorial",
      "objectives": [],
      "syllabus": [
          {
              "title": "JS Operators",
              "sub_sections": [
                  {"title": "JS Operators", "description": None},
                  {"title": "JS Arithmetic", "description": None},
                  ...
              ]
          },
          ...
      ]
  }
  ```

### `generator.py` — Markdown Generator
- Accepts the structured dict from **either** parser (the shape is identical).
- Builds a markdown string preserving original ordering.
- Skips the "What You Will Learn" block when `objectives` is empty (the W3Schools case) and omits description lines when `description` is `None`.
- Saves the file to `Markdown files/<slug>.md`.
- Returns the output file path.

### `templates/index.html` — UI Template
- Single input field accepting a Udemy course URL **or** a W3Schools tutorial URL.
- Submit button triggers the `/extract` POST request.
- Displays success message with a download link, or an error message on failure.

---

## Data Model

Both sources share one intermediate dict so the generator never branches on source:

```python
Document = {
    "title": str,                 # Udemy course title / W3Schools subject name
    "objectives": list[str],      # Udemy only; [] for W3Schools
    "syllabus": list[Section],
}

Section = {
    "title": str,
    "sub_sections": list[SubSection]
}

SubSection = {
    "title": str,
    "description": str | None   # Udemy only; always None for W3Schools
}
```

The only structural difference between sources is depth of information, not shape: W3Schools fills `objectives` with `[]` and every `description` with `None`, collapsing the effective model to 2 levels (section → sub-section) while keeping the 3-level container.

---

## Markdown Output Format

### Udemy (objectives + descriptions)
```markdown
# Course Title

## What You Will Learn
- Objective 1
- Objective 2

---

## Section 1: <Section Title>

### <Sub-section Title>
<Description if present>

### <Sub-section Title>
<!-- no description -->

## Section 2: <Section Title>
...
```

### W3Schools (no objectives, no descriptions)
```markdown
# JS Tutorial

---

## Section 1: JS Operators

### JS Operators

### JS Arithmetic

## Section 2: JS Strings
...
```

---

## Directory Structure (final)

```
Udemy Syllabus Extractor/
├── HTML Files/                 # Downloaded Udemy/W3Schools HTML pages
├── Markdown files/             # Generated markdown output
├── templates/
│   └── index.html              # Web UI template
├── app.py                      # Flask entry point + routes + source router
├── downloader.py               # Udemy HTML download logic (Playwright)
├── w3schools_downloader.py     # W3Schools static HTML download logic
├── parser.py                   # Udemy BeautifulSoup parser
├── w3schools_parser.py         # W3Schools BeautifulSoup parser
├── generator.py                # Shared markdown file generator
├── requirements.txt            # Python dependencies
├── venv/                       # Virtual environment (not committed)
├── CLAUDE.md
├── specs.md
└── design.md
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `flask` | Web server and UI routing |
| `requests` | Downloading W3Schools (static) HTML pages |
| `playwright` | Downloading Udemy (JS-rendered) HTML pages |
| `beautifulsoup4` | Parsing HTML |
| `lxml` | Fast HTML parser backend for BeautifulSoup |

Install with:
```bash
pip install flask requests playwright beautifulsoup4 lxml
playwright install chromium
```

---

## Build Steps (Phase 1 — Udemy, completed)

The project was built incrementally in the following order. Each step is independently testable before moving to the next.

### Step 1 — Project Setup
- Confirm `venv` is active.
- Create `requirements.txt` with `flask`, `requests`, `beautifulsoup4`, `lxml`.
- Run `pip install -r requirements.txt`.
- Create the `Markdown files/` directory.
- Create empty placeholder files: `app.py`, `downloader.py`, `parser.py`, `generator.py`.

### Step 2 — HTML Downloader (`downloader.py`)
- Implement `download(url: str) -> str` that saves the page HTML to `HTML Files/` and returns the file path.
- Test manually: call the function with a real Udemy URL and confirm the HTML file is saved.

### Step 3 — HTML Parser (`parser.py`)
- Implement `parse(html_path: str) -> dict` using BeautifulSoup.
- Extract course objectives using the known CSS class.
- Extract syllabus panels, then section titles, sub-section titles, and optional descriptions within each panel.
- Test with the downloaded HTML file and print the resulting dict to verify structure and ordering.

### Step 4 — Markdown Generator (`generator.py`)
- Implement `generate(data: dict, course_slug: str) -> str` that writes the markdown file and returns its path.
- Test by passing the parsed dict from Step 3 and inspecting the output file.

### Step 5 — Web UI (`app.py` + `templates/index.html`)
- Create the Flask app with a `GET /` route serving `index.html`.
- Create the `POST /extract` route that calls downloader → parser → generator in sequence.
- Create `templates/index.html` with a URL input form.
- Run the app and test the full flow end-to-end in a browser.

### Step 6 — Polish and Error Handling
- Handle invalid URLs, network failures, and missing HTML elements gracefully.
- Show user-friendly error messages in the UI.
- Validate that the `HTML Files/` and `Markdown files/` directories exist on startup, creating them if not.

---

## Build Phases (Phase 2 — W3Schools support)

This is a **completely new set of phases** that adds W3Schools tutorial extraction on top of the existing Udemy pipeline. The guiding principle is *reuse the generator unchanged* by making the new parser emit the same intermediate dict shape. Each phase is independently testable before moving on. A reference page (`HTML Files/JavaScript Tutorial.html`, from `https://www.w3schools.com/js/default.asp`) is already saved for offline development.

### Phase 2.0 — Dependencies & Scaffolding
- Add `requests` to `requirements.txt` (used for the static W3Schools download) and run `pip install -r requirements.txt`.
- Create empty placeholder modules: `w3schools_downloader.py` and `w3schools_parser.py`.
- No behavior change to the existing Udemy flow.

### Phase 2.1 — Source Router
- Add a `detect_source(url: str) -> "udemy" | "w3schools"` helper (in `app.py` or a new `source.py`) that inspects the URL host.
- Return a clear validation error for any unsupported host.
- Unit-test with sample Udemy and W3Schools URLs; confirm correct routing and that junk URLs are rejected.

### Phase 2.2 — W3Schools Downloader (`w3schools_downloader.py`)
- Implement `download(url: str) -> str` that fetches the static page with `requests` (set a desktop `User-Agent`), derives a slug from the URL path (e.g. `js/default.asp` → `js-default`), saves to `HTML Files/<slug>.html`, and returns the path.
- No Playwright, no section expansion — the menu is fully present in the static HTML.
- Test manually against a live W3Schools URL and confirm the saved file contains `id="leftmenuinnerinner"`.

### Phase 2.3 — W3Schools Parser (`w3schools_parser.py`)
- Implement `parse(html_path: str) -> dict` using BeautifulSoup, returning the shared dict shape (`title`, `objectives`, `syllabus`).
- Locate the menu container (`id="leftmenuinnerinner"`); read the subject name from `<h2 class="left">`.
- Walk the container's direct children in document order: each top-level `<a target="_top">` starts a section; an immediately following `<div class="tut_overview">` supplies that section's sub-sections from its inner `<a target="_top">` items.
- Set `objectives` to `[]` and every sub-section's `description` to `None`.
- Handle edge cases: section `<a>` with no following `tut_overview` (empty `sub_sections`); first item in a `tut_overview` repeating the section name (keep it, do not deduplicate); the `tut_overview overview_body` class variant and the `-height-0` item-class variant.
- Test against `HTML Files/JavaScript Tutorial.html`; print the dict and verify section/sub-section count and ordering match the page.

### Phase 2.4 — Generator Compatibility
- Confirm `generator.generate(data)` already produces correct output for the W3Schools dict (empty objectives → skip "What You Will Learn"; `None` descriptions → no description lines).
- Adjust the generator only if a branch still assumes objectives/descriptions exist; keep it source-agnostic.
- Test by feeding the Phase 2.3 dict to the generator and inspecting the markdown.

### Phase 2.5 — Wire Into the Web Flow (`app.py`)
- In `/extract`, call the source router, then dispatch to the matching downloader + parser, then the shared generator.
- Relax URL validation to accept either `udemy.com` or `w3schools.com`.
- Return the same JSON response shape (title, filename, counts, download URL); `objectives` count will be `0` for W3Schools.

### Phase 2.6 — UI Update (`templates/index.html`)
- Update the label/placeholder/subtitle to indicate both Udemy and W3Schools URLs are accepted.
- Ensure the success panel reads sensibly when `objectives` is `0` (e.g. show only the section count).

### Phase 2.7 — End-to-End Test & Polish
- Run the app and extract a W3Schools tutorial end-to-end in the browser; confirm the markdown downloads and ordering is faithful.
- Re-run a Udemy extraction to confirm no regression.
- Add user-friendly errors for unsupported hosts, network failures, and a missing/empty `leftmenuinnerinner` container (e.g. a non-tutorial W3Schools page).
