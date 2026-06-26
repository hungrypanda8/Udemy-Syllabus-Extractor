import os
import re
from playwright.sync_api import sync_playwright


def _slug_from_url(url: str) -> str:
    match = re.search(r"/course/([^/?#]+)", url)
    if not match:
        raise ValueError(f"Could not extract course slug from URL: {url}")
    return match.group(1)


def download(url: str) -> str:
    """Download a Udemy course page (fully JS-rendered) and save to HTML Files/.

    Expands all collapsed curriculum sections before saving so the full
    syllabus is present in the HTML.  Returns the local file path.
    """
    slug = _slug_from_url(url)
    output_dir = os.path.join(os.path.dirname(__file__), "HTML Files")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{slug}.html")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )

        page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        # Wait for the curriculum to appear
        page.wait_for_selector("[class*='curriculum-section']", timeout=30_000)

        # Expand all collapsed sections by clicking their toggle buttons
        _expand_all_sections(page)

        html = page.content()
        browser.close()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path


def _expand_all_sections(page) -> None:
    """Click every collapsed curriculum section panel to expand it."""
    # Panels that are NOT already expanded have no _expanded_ class
    collapsed = page.query_selector_all("[class*='_panel_'][class*='curriculum-section']:not([class*='_expanded_'])")
    for panel in collapsed:
        try:
            toggle = panel.query_selector("button")
            if toggle:
                toggle.click()
                page.wait_for_timeout(200)
        except Exception:
            pass
