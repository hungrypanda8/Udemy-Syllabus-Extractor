# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
A Python GUI application that extracts course syllabi from Udemy course pages and generates structured markdown files. The output is intended for use by an AI chatbot that teaches the course content in order.

## How It Works
1. User pastes a Udemy course URL into a browser-based UI.
2. Program downloads the HTML page into "HTML Files/".
3. Parses the HTML to extract:
   **Course objectives** from elements with class `what-you-will-learn-module-scss-module__BBo-EG__objective-item`
   **Syllabus** structured as sections, sub-sections, and sub-section descriptions (only some sub-sections have descriptions).
4. Generates a markdown file saved to "Markdown files/".

## HTML Parsing Classes (Udemy-specific)
* **Panel (one section + its sub-sections):** `_panel_xk1nn_16 curriculum-section-module-scss-module__9JCrHq__panel _expanded_xk1nn_56`
* **Section title:** `curriculum-section-module-scss-module__9JCrHq__section-title` 
* **Sub-section title:** `curriculum-section-module-scss-module__9JCrHq__course-lecture-title`
* **Sub-section description:** `curriculum-section-module-scss-module__9JCrHq__hidden-on-mobile curriculum-section-module-scss-module__9JCrHq__item-description ud-text-sm`

## Environment
* **Python:** 3.11.3
* **Virtual environments:** `venv`
* **Activate:** `venv\Scripts\activate` (Windows)
* **Dependencies:** No dependencies installed yet; will need an HTML parser (e.g., BeautifulSoup) and a web framework for the UI.

## Key Constraints
* Python only (no other languages).
* Markdown output must preserve the exact ordering of sections/subsections/descriptions as they appear in the HTML.
* The syllabus is stored as a 3-dimensional array (section -> sub-section -> description).
* Sub-section descriptions are optional - not every sub-section has one.

## Directory Structure
* `HTML Files/`: Downloaded Udemy course HTML pages and their assets.
* `Markdown files/`: Generated markdown output (to be created).

## Important Instructions
* **Do NOT read or explore the `venv/` folder.** It contains the Python virtual environment and is not part of the application source code.