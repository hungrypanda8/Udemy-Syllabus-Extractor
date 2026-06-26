"""Flask web server for the Udemy Syllabus Extractor.

Serves a single-page UI where the user pastes a Udemy course URL. On submit,
the ``/extract`` endpoint runs the pipeline (downloader -> parser -> generator)
and returns the generated markdown file's name so the UI can offer a download.
"""

import os

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_from_directory,
)

import downloader
import generator
import parser as html_parser

BASE_DIR = os.path.dirname(__file__)
HTML_DIR = os.path.join(BASE_DIR, "HTML Files")
MARKDOWN_DIR = os.path.join(BASE_DIR, "Markdown files")

app = Flask(__name__)


def _ensure_directories() -> None:
    """Create the working directories if they do not already exist."""
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(MARKDOWN_DIR, exist_ok=True)


@app.route("/", methods=["GET"])
def index():
    """Serve the single-page UI."""
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():
    """Run the full extraction pipeline for a submitted Udemy URL.

    Expects a JSON body of the form ``{"url": "..."}``. Returns JSON describing
    the generated markdown file, or an error message with an appropriate HTTP
    status code on failure.
    """
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()

    if not url:
        return jsonify({"error": "Please provide a Udemy course URL."}), 400

    if "udemy.com" not in url:
        return jsonify({"error": "That does not look like a Udemy course URL."}), 400

    try:
        html_path = downloader.download(url)
    except Exception as exc:  # noqa: BLE001 - surface any download failure
        return jsonify({"error": f"Failed to download the course page: {exc}"}), 502

    try:
        parsed = html_parser.parse(html_path)
    except Exception as exc:  # noqa: BLE001 - surface any parse failure
        return jsonify({"error": f"Failed to parse the course page: {exc}"}), 500

    try:
        markdown_path = generator.generate(parsed)
    except Exception as exc:  # noqa: BLE001 - surface any generation failure
        return jsonify({"error": f"Failed to generate the markdown file: {exc}"}), 500

    filename = os.path.basename(markdown_path)
    return jsonify(
        {
            "title": parsed.get("title"),
            "filename": filename,
            "objectives": len(parsed.get("objectives") or []),
            "sections": len(parsed.get("syllabus") or []),
            "download_url": f"/download/{filename}",
        }
    )


@app.route("/download/<path:filename>", methods=["GET"])
def download_markdown(filename):
    """Serve a generated markdown file as a download."""
    return send_from_directory(MARKDOWN_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    _ensure_directories()
    app.run(debug=True, port=5000)
