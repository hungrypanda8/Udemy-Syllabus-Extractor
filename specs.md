# Syllabus Extractor — Project Specifications

## Purpose
Extract course/tutorial syllabi from supported learning sites and generate structured markdown files suitable for use by an AI chatbot that teaches content in order. Two sources are supported: **Udemy** course pages and **W3Schools** tutorial pages.

## Supported Sources
| Source | Example URL | Rendering | Objectives | Syllabus depth |
|---|---|---|---|---|
| Udemy | `https://www.udemy.com/course/<slug>/` | JS-rendered (Playwright); collapsed sections expanded before saving | Yes | 3-level: section → sub-section → optional description |
| W3Schools | `https://www.w3schools.com/js/default.asp` | Static HTML (plain download) | No | 2-level: section → sub-section |

The source is detected from the URL host (`udemy.com` vs `w3schools.com`) and the matching downloader/parser is selected. Both parsers emit the same intermediate dict, so the markdown generator is shared.

## User Flow
1. User pastes a Udemy course URL **or** a W3Schools tutorial URL into the browser-based UI.
2. Application detects the source, then downloads the HTML page into `HTML Files/`.
3. HTML is parsed to extract the syllabus structure (and, for Udemy, course objectives).
4. A markdown file is generated and saved to `Markdown files/`.

## Parsing Targets — Udemy

### Course Objectives
- **Element class:** `what-you-will-learn-module-scss-module__BBo-EG__objective-item`

### Syllabus Structure (3-dimensional: section → sub-section → description)
| Element | HTML Class |
|---|---|
| Panel (section + sub-sections) | `_panel_xk1nn_16 curriculum-section-module-scss-module__9JCrHq__panel _expanded_xk1nn_56` |
| Section title | `curriculum-section-module-scss-module__9JCrHq__section-title` |
| Sub-section title | `curriculum-section-module-scss-module__9JCrHq__course-lecture-title` |
| Sub-section description | `curriculum-section-module-scss-module__9JCrHq__hidden-on-mobile curriculum-section-module-scss-module__9JCrHq__item-description ud-text-sm` |

## Parsing Targets — W3Schools

The whole syllabus lives in the left navigation menu. Markers are a mix of an `id`, classes, and `target` attributes (verified against `HTML Files/JavaScript Tutorial.html`):

### Syllabus Structure (2-dimensional: section → sub-section)
| Element | HTML Marker |
|---|---|
| Menu container (whole syllabus) | `id="leftmenuinnerinner"` |
| Subject name (overall title, e.g. "JS Tutorial") | `<h2 class="left">` inside the menu container |
| Section | top-level `<a target="_top">` that is a direct child of the menu container |
| Sub-section list | `<div class="tut_overview">` (may also be `tut_overview overview_body`) immediately following the section `<a>` |
| Sub-section item | `<a target="_top">` inside the `tut_overview` div (may also carry a `-height-0` class) |

W3Schools edge cases:
- A section `<a>` may have **no** following `tut_overview` div → standalone section with zero sub-sections.
- The first `<a>` in a `tut_overview` often repeats the section name; keep it to preserve faithful ordering.

## Output Format
- One markdown file per course/tutorial.
- Preserves exact ordering of sections, sub-sections, and (Udemy) descriptions as they appear in the HTML.
- Sub-section descriptions are optional and Udemy-only — not every Udemy sub-section has one, and W3Schools has none.
- For W3Schools, `objectives` is empty and every sub-section's `description` is `None`, so the generator emits the syllabus only.

## Technical Stack
- **Language:** Python 3.11.3 only (no other languages).
- **UI:** Browser-based (Flask).
- **HTML Parsing:** BeautifulSoup.
- **Udemy download:** Playwright (Chromium) for JS rendering; W3Schools uses a plain static fetch (e.g. `requests`) since no rendering is needed.
- **Virtual environment:** `venv` — activate with `venv\Scripts\activate` on Windows.

## Directory Structure
```
Udemy Syllabus Extractor/
├── HTML Files/          # Downloaded Udemy/W3Schools HTML pages and assets
├── Markdown files/      # Generated markdown output
├── venv/                # Python virtual environment
└── specs.md             # This file
```

## Constraints
- Python only.
- Markdown output must preserve original HTML ordering.
- Syllabus data model: Udemy is `syllabus[section][sub_section][description]`; W3Schools is `syllabus[section][sub_section]` (descriptions always `None`).
- Sub-section descriptions are optional and Udemy-only.
- Both sources must normalize to one shared intermediate dict so the generator stays source-agnostic.
