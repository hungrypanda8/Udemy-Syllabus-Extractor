# Udemy Syllabus Extractor — Project Specifications

## Purpose
Extract course syllabi from Udemy course pages and generate structured markdown files suitable for use by an AI chatbot that teaches course content in order.

## User Flow
1. User pastes a Udemy course URL into the browser-based UI.
2. Application downloads the HTML page into `HTML Files/`.
3. HTML is parsed to extract course objectives and syllabus structure.
4. A markdown file is generated and saved to `Markdown files/`.

## Parsing Targets

### Course Objectives
- **Element class:** `what-you-will-learn-module-scss-module__BBo-EG__objective-item`

### Syllabus Structure (3-dimensional: section → sub-section → description)
| Element | HTML Class |
|---|---|
| Panel (section + sub-sections) | `_panel_xk1nn_16 curriculum-section-module-scss-module__9JCrHq__panel _expanded_xk1nn_56` |
| Section title | `curriculum-section-module-scss-module__9JCrHq__section-title` |
| Sub-section title | `curriculum-section-module-scss-module__9JCrHq__course-lecture-title` |
| Sub-section description | `curriculum-section-module-scss-module__9JCrHq__hidden-on-mobile curriculum-section-module-scss-module__9JCrHq__item-description ud-text-sm` |

## Output Format
- Markdown file per course.
- Preserves exact ordering of sections, sub-sections, and descriptions as they appear in the HTML.
- Sub-section descriptions are optional — not every sub-section has one.

## Technical Stack
- **Language:** Python 3.11.3 only (no other languages).
- **UI:** Browser-based (web framework TBD — e.g., Flask, FastAPI).
- **HTML Parsing:** BeautifulSoup (to be installed).
- **Virtual environment:** `venv` — activate with `venv\Scripts\activate` on Windows.
- **Dependencies:** None installed yet; requires an HTML parser and a web framework.

## Directory Structure
```
Udemy Syllabus Extractor/
├── HTML Files/          # Downloaded Udemy course HTML pages and assets
├── Markdown files/      # Generated markdown output
├── venv/                # Python virtual environment
└── specs.md             # This file
```

## Constraints
- Python only.
- Markdown output must preserve original HTML ordering.
- Syllabus data model is a 3-dimensional array: `syllabus[section][sub_section][description]`.
- Sub-section descriptions are optional.
