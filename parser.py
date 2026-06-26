"""HTML Parser for Udemy course pages.

Extracts course objectives and the syllabus (sections -> sub-sections ->
optional descriptions) from a locally saved Udemy course HTML file using
BeautifulSoup. The output preserves the exact ordering of sections,
sub-sections, and descriptions as they appear in the HTML.
"""

import os

from bs4 import BeautifulSoup


def parse(html_path: str) -> dict:
    """Parse a saved Udemy course HTML file into a structured dict.

    Args:
        html_path: Path to a local HTML file saved by ``downloader.download``.

    Returns:
        A dict of the form::

            {
                "title": "Course Title",
                "objectives": ["...", "..."],
                "syllabus": [
                    {
                        "title": "Section Title",
                        "sub_sections": [
                            {"title": "Lecture Title", "description": str | None},
                            ...
                        ],
                    },
                    ...
                ],
            }
    """
    if not os.path.isfile(html_path):
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "lxml")

    return {
        "title": _extract_title(soup),
        "objectives": _extract_objectives(soup),
        "syllabus": _extract_syllabus(soup),
    }


def _extract_title(soup) -> str:
    """Return the course title, falling back to the page <title>."""
    heading = soup.select_one("h1")
    if heading and heading.get_text(strip=True):
        return heading.get_text(strip=True)
    if soup.title and soup.title.get_text(strip=True):
        return soup.title.get_text(strip=True)
    return "Untitled Course"


def _extract_objectives(soup) -> list:
    """Return the 'What you'll learn' objectives in document order."""
    objectives = []
    for item in soup.select('[class*="objective-item"]'):
        text = item.get_text(" ", strip=True)
        if text:
            objectives.append(text)
    return objectives


def _extract_syllabus(soup) -> list:
    """Return the syllabus as an ordered list of sections.

    Each panel corresponds to one section. Within a panel, sub-sections are
    the lecture titles in document order; a sub-section's optional description
    is the ``item-description`` element nested in the same list item.
    """
    syllabus = []
    panels = soup.select('[class*="_panel_"][class*="curriculum-section"]')

    for panel in panels:
        section_title = _section_title(panel)
        sub_sections = []

        for lecture in panel.select('[class*="course-lecture-title"]'):
            sub_sections.append(
                {
                    "title": lecture.get_text(" ", strip=True),
                    "description": _lecture_description(lecture),
                }
            )

        syllabus.append({"title": section_title, "sub_sections": sub_sections})

    return syllabus


def _section_title(panel) -> str:
    """Return the title text for a section panel."""
    # The wrapping "section-title-container" also matches a bare substring
    # search and carries the lecture-count/duration stats, so exclude it and
    # read only the inner section-title element.
    title_el = panel.select_one(
        '[class*="__section-title"]:not([class*="section-title-container"])'
    )
    if title_el:
        return title_el.get_text(" ", strip=True)
    return ""


def _lecture_description(lecture):
    """Return the description for a lecture sub-section, or None.

    The description lives inside the ``ud-block-list-item-content`` wrapper
    that also holds the lecture title. A toggle button shares the substring
    ``item-description`` in its class, so we match the module-prefixed
    ``__item-description`` token to select the real description element.
    """
    item = lecture
    while item is not None:
        item = item.parent
        classes = item.get("class") if item is not None and hasattr(item, "get") else None
        if classes and "ud-block-list-item-content" in classes:
            break
    else:
        return None

    if item is None:
        return None

    desc_el = item.select_one('[class*="__item-description"]')
    if desc_el:
        text = desc_el.get_text(" ", strip=True)
        if text:
            return text
    return None


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # Default to the first HTML file available for a quick manual test.
        html_dir = os.path.join(os.path.dirname(__file__), "HTML Files")
        files = [f for f in os.listdir(html_dir) if f.endswith(".html")]
        if not files:
            raise SystemExit("No HTML files found in 'HTML Files/'.")
        path = os.path.join(html_dir, files[0])

    result = parse(path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
