"""HTML parser for W3Schools tutorial pages.

Extracts the subject name and a 2-level syllabus (section -> sub-section)
from a locally saved W3Schools tutorial HTML file using BeautifulSoup.

The output uses the **same** intermediate dict shape as ``parser.py`` so the
markdown generator stays source-agnostic.  W3Schools has no course objectives
and no sub-section descriptions, so ``objectives`` is always ``[]`` and every
sub-section's ``description`` is ``None``.  Ordering of sections and
sub-sections is preserved exactly as it appears in the left-menu container.
"""

import os

from bs4 import BeautifulSoup


def parse(html_path: str) -> dict:
    """Parse a saved W3Schools tutorial HTML file into a structured dict.

    Args:
        html_path: Path to a local HTML file saved by
            ``w3schools_downloader.download``.

    Returns:
        A dict of the form::

            {
                "title": "JS Tutorial",
                "objectives": [],
                "syllabus": [
                    {
                        "title": "JS Operators",
                        "sub_sections": [
                            {"title": "JS Operators", "description": None},
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

    menu = soup.find(id="leftmenuinnerinner")
    if menu is None:
        raise ValueError(
            "Could not find the W3Schools menu container "
            "(id='leftmenuinnerinner'); is this a tutorial page?"
        )

    return {
        "title": _extract_title(menu),
        "objectives": [],
        "syllabus": _extract_syllabus(menu),
    }


def _extract_title(menu) -> str:
    """Return the subject name from the menu's ``<h2 class="left">``."""
    heading = menu.find("h2", class_="left")
    if heading and heading.get_text(strip=True):
        return heading.get_text(strip=True)
    return "Untitled Tutorial"


def _is_section_link(el) -> bool:
    """True if ``el`` is a top-level section ``<a target="_top">``."""
    return (
        getattr(el, "name", None) == "a"
        and el.get("target") == "_top"
    )


def _is_tut_overview(el) -> bool:
    """True if ``el`` is a ``tut_overview`` sub-section container div."""
    if getattr(el, "name", None) != "div":
        return False
    classes = el.get("class") or []
    return "tut_overview" in classes


def _extract_syllabus(menu) -> list:
    """Return the syllabus as an ordered list of sections.

    Walks the menu container's direct children in document order.  Each
    top-level ``<a target="_top">`` opens a new section; if its immediately
    following sibling is a ``tut_overview`` div, that div's inner
    ``<a target="_top">`` elements become the section's sub-sections.  A
    section link with no following ``tut_overview`` is a standalone section
    with an empty ``sub_sections`` list.
    """
    syllabus = []

    children = [c for c in menu.children if getattr(c, "name", None)]
    i = 0
    while i < len(children):
        el = children[i]
        if not _is_section_link(el):
            i += 1
            continue

        section = {
            "title": el.get_text(" ", strip=True),
            "sub_sections": [],
        }

        # The sub-section list, if any, is the very next element sibling.
        if i + 1 < len(children) and _is_tut_overview(children[i + 1]):
            overview = children[i + 1]
            for link in overview.find_all("a", target="_top"):
                section["sub_sections"].append(
                    {
                        "title": link.get_text(" ", strip=True),
                        "description": None,
                    }
                )
            i += 2
        else:
            i += 1

        syllabus.append(section)

    return syllabus


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.path.join(
            os.path.dirname(__file__), "HTML Files", "JavaScript Tutorial.html"
        )

    result = parse(path)
    print(json.dumps(result, indent=2, ensure_ascii=False))
