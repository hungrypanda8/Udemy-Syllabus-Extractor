# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
A Python GUI application that extracts course syllabi from online learning pages and generates structured markdown files. The output is intended for use by an AI chatbot that teaches the course content in order. Two sources are supported:
* **Udemy** course pages.
* **W3Schools** tutorial pages (e.g. `https://www.w3schools.com/js/default.asp`).

The source is detected automatically from the pasted URL (`udemy.com` vs `w3schools.com`), and the matching downloader/parser is used. Both sources produce the same intermediate data structure, so a single markdown generator serves both.

## How It Works
1. User pastes a course/tutorial URL into a browser-based UI.
2. The program detects the source from the URL and downloads the HTML page into "HTML Files/".
3. Parses the HTML to extract a syllabus structure (see per-source classes below).
4. Generates a markdown file saved to "Markdown files/".

### Udemy flow
* Downloads a fully JS-rendered page (Playwright) and expands all collapsed curriculum sections first.
* Extracts **course objectives** and a 3-level syllabus (section → sub-section → optional description).

### W3Schools flow
* Downloads the static HTML page (no JS rendering or section expansion required).
* Extracts a 2-level syllabus (section → sub-section). W3Schools has **no objectives** and **no sub-section descriptions**.

## HTML Parsing Classes (Udemy-specific)
* **Panel (one section + its sub-sections):** `_panel_xk1nn_16 curriculum-section-module-scss-module__9JCrHq__panel _expanded_xk1nn_56`
* **Section title:** `curriculum-section-module-scss-module__9JCrHq__section-title` 
* **Sub-section title:** `curriculum-section-module-scss-module__9JCrHq__course-lecture-title`
* **Sub-section description:** `curriculum-section-module-scss-module__9JCrHq__hidden-on-mobile curriculum-section-module-scss-module__9JCrHq__item-description ud-text-sm`

## HTML Parsing Markers (W3Schools-specific)
The entire syllabus lives inside the left navigation menu. Note that the markers are a mix of an `id`, classes, and `target` attributes (verified against the saved `HTML Files/JavaScript Tutorial.html`):

* **Menu container (holds the whole syllabus):** element with `id="leftmenuinnerinner"`.
* **Subject name (the overall title, e.g. "JS Tutorial"):** `<h2 class="left">` inside the menu container.
* **Section:** a top-level `<a target="_top">` that is a direct child of the menu container (e.g. "JS Operators", "JS Strings").
* **Sub-section list:** a `<div class="tut_overview">` (may also appear as `tut_overview overview_body`) that immediately follows its section's `<a>`.
* **Sub-section item:** an `<a target="_top">` inside the `tut_overview` div (these may also carry a `-height-0` class on some pages).

Notes for the parser:
* Some top-level section `<a>` elements have **no** following `tut_overview` div — they are standalone sections with no sub-sections (e.g. "JS Home", "JS Introduction").
* The first `<a>` inside a `tut_overview` div often repeats the section name; preserve it as-is to keep ordering faithful (do not deduplicate).

## Environment
* **Python:** 3.11.3
* **Virtual environments:** `venv`
* **Activate:** `venv\Scripts\activate` (Windows)
* **Dependencies:** No dependencies installed yet; will need an HTML parser (e.g., BeautifulSoup) and a web framework for the UI.

## Key Constraints
* Python only (no other languages).
* Markdown output must preserve the exact ordering of sections/subsections/descriptions as they appear in the HTML.
* The syllabus is stored as a nested array (Udemy: section → sub-section → description; W3Schools: section → sub-section).
* Sub-section descriptions are optional and Udemy-only - not every sub-section has one, and W3Schools has none.
* Both sources normalize to the same intermediate dict shape so the markdown generator stays source-agnostic. W3Schools simply yields an empty `objectives` list and `description: None` on every sub-section.

## Directory Structure
* `HTML Files/`: Downloaded Udemy/W3Schools HTML pages and their assets.
* `Markdown files/`: Generated markdown output (to be created).