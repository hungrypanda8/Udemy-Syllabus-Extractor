"""W3Schools HTML downloader.

Fetches a W3Schools tutorial page as **static** HTML with a plain HTTP
request (no JS rendering, no section expansion -- the left-menu syllabus is
fully present in the raw HTML).  The page is saved to ``HTML Files/<slug>.html``
and the local file path is returned.
"""

import os
from urllib.parse import urlparse

import requests

# A desktop User-Agent; W3Schools serves the full menu to ordinary browsers.
_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


def _slug_from_url(url: str) -> str:
    """Derive a filesystem-friendly slug from a W3Schools URL path.

    e.g. ``https://www.w3schools.com/js/default.asp`` -> ``js-default``.
    """
    path = urlparse(url).path.strip("/")
    if not path:
        raise ValueError(f"Could not extract a tutorial slug from URL: {url}")

    # Drop the file extension (.asp/.html) from the last path segment.
    segments = path.split("/")
    segments[-1] = os.path.splitext(segments[-1])[0]
    slug = "-".join(segment for segment in segments if segment)

    if not slug:
        raise ValueError(f"Could not extract a tutorial slug from URL: {url}")
    return slug


def download(url: str) -> str:
    """Download a W3Schools tutorial page and save it to ``HTML Files/``.

    Returns the local file path.
    """
    slug = _slug_from_url(url)
    output_dir = os.path.join(os.path.dirname(__file__), "HTML Files")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{slug}.html")

    response = requests.get(url, headers={"User-Agent": _USER_AGENT}, timeout=30)
    response.raise_for_status()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    return output_path
