"""Markdown Generator for parsed Udemy course data.

Takes the structured dict produced by ``parser.parse`` and writes a markdown
file to ``Markdown files/``. The output preserves the exact ordering of
sections, sub-sections, and descriptions as they appear in the HTML.

The generated file is named after the course title (slugified), so the saved
markdown is recognisable by its course name rather than a URL slug.
"""

import os
import re


def _slugify(text: str) -> str:
    """Turn a course title into a safe, lower-case filename slug.

    Strips characters that are illegal in file names, collapses whitespace and
    punctuation into single hyphens, and trims leading/trailing hyphens.
    """
    text = text.strip().lower()
    # Replace any run of non-alphanumeric characters with a single hyphen.
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "course"


def generate(data: dict, course_slug: str | None = None) -> str:
    """Write a markdown file for the parsed course data and return its path.

    Args:
        data: The structured dict from ``parser.parse`` containing
            ``title``, ``objectives``, and ``syllabus``.
        course_slug: Optional fallback slug for the filename (e.g. the URL
            slug). When omitted, the filename is derived from the course title.

    Returns:
        The path to the written markdown file.
    """
    title = (data.get("title") or "Untitled Course").strip()

    # Name the file after the course title; fall back to the URL slug.
    filename_base = _slugify(title) if title and title != "Untitled Course" else None
    if not filename_base:
        filename_base = _slugify(course_slug) if course_slug else "course"

    output_dir = os.path.join(os.path.dirname(__file__), "Markdown files")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{filename_base}.md")

    markdown = _build_markdown(data, title)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    return output_path


def _build_markdown(data: dict, title: str) -> str:
    """Build the full markdown document as a single string."""
    lines = [f"# {title}", ""]

    objectives = data.get("objectives") or []
    if objectives:
        lines.append("## What You Will Learn")
        lines.append("")
        for objective in objectives:
            lines.append(f"- {objective}")
        lines.append("")

    lines.append("---")
    lines.append("")

    syllabus = data.get("syllabus") or []
    for index, section in enumerate(syllabus, start=1):
        section_title = section.get("title") or f"Section {index}"
        lines.append(f"## Section {index}: {section_title}")
        lines.append("")

        for sub_section in section.get("sub_sections") or []:
            sub_title = sub_section.get("title") or ""
            lines.append(f"### {sub_title}")
            description = sub_section.get("description")
            if description:
                lines.append(description)
            lines.append("")

    # Collapse to a single trailing newline.
    return "\n".join(lines).rstrip("\n") + "\n"


if __name__ == "__main__":
    import sys

    import parser as html_parser

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # Default to the first HTML file available for a quick manual test.
        html_dir = os.path.join(os.path.dirname(__file__), "HTML Files")
        files = [f for f in os.listdir(html_dir) if f.endswith(".html")]
        if not files:
            raise SystemExit("No HTML files found in 'HTML Files/'.")
        path = os.path.join(html_dir, files[0])

    parsed = html_parser.parse(path)
    out = generate(parsed)
    print(f"Markdown written to: {out}")
