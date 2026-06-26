# Udemy Syllabus Extractor — Design Document

## Architecture Overview

The application follows a simple three-layer pipeline:

```
[Web UI] → [Downloader] → [Parser] → [Markdown Generator]
```

All layers are pure Python. The web UI is served locally via a lightweight framework (Flask). No database is used; state lives only in memory during a single extraction run.

---

## Module Breakdown

### `app.py` — Web Server / Entry Point
- Starts the Flask development server.
- Serves the single-page UI.
- Exposes a POST endpoint (`/extract`) that accepts a Udemy URL and returns the path to the generated markdown file.

### `downloader.py` — HTML Downloader
- Accepts a Udemy course URL.
- Downloads the full HTML of the page using `requests`.
- Saves the raw HTML to `HTML Files/<course-slug>.html`.
- Returns the local file path.

### `parser.py` — HTML Parser
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

### `generator.py` — Markdown Generator
- Accepts the structured dict from `parser.py`.
- Builds a markdown string preserving original ordering.
- Saves the file to `Markdown files/<course-slug>.md`.
- Returns the output file path.

### `templates/index.html` — UI Template
- Single input field for the Udemy URL.
- Submit button triggers the `/extract` POST request.
- Displays success message with a download link, or an error message on failure.

---

## Data Model

```python
# Syllabus 3D structure
syllabus: list[Section]

Section = {
    "title": str,
    "sub_sections": list[SubSection]
}

SubSection = {
    "title": str,
    "description": str | None   # optional
}
```

---

## Markdown Output Format

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

---

## Directory Structure (final)

```
Udemy Syllabus Extractor/
├── HTML Files/          # Downloaded Udemy HTML pages
├── Markdown files/      # Generated markdown output
├── templates/
│   └── index.html       # Web UI template
├── app.py               # Flask entry point + routes
├── downloader.py        # HTML download logic
├── parser.py            # BeautifulSoup HTML parser
├── generator.py         # Markdown file generator
├── requirements.txt     # Python dependencies
├── venv/                # Virtual environment (not committed)
├── CLAUDE.md
├── specs.md
└── design.md
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `flask` | Web server and UI routing |
| `requests` | Downloading Udemy HTML pages |
| `beautifulsoup4` | Parsing HTML |
| `lxml` | Fast HTML parser backend for BeautifulSoup |

Install with:
```bash
pip install flask requests beautifulsoup4 lxml
```

---

## Build Steps

The project will be built incrementally in the following order. Each step is independently testable before moving to the next.

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
