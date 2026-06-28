"""Source router: maps a pasted URL to its supported source.

The application supports two sources, detected from the URL host:

* ``udemy.com``     -> ``"udemy"``
* ``w3schools.com`` -> ``"w3schools"``

Any other host raises ``ValueError`` so the caller can surface a clear
validation error to the UI.
"""

from urllib.parse import urlparse

# Map of recognised host suffixes to the source name used elsewhere.
_SUPPORTED_HOSTS = {
    "udemy.com": "udemy",
    "w3schools.com": "w3schools",
}


def detect_source(url: str) -> str:
    """Return the source name (``"udemy"`` or ``"w3schools"``) for ``url``.

    Raises ``ValueError`` if the URL is empty, malformed, or points at an
    unsupported host.
    """
    if not url or not url.strip():
        raise ValueError("Please provide a course or tutorial URL.")

    host = (urlparse(url.strip()).hostname or "").lower()
    if not host:
        raise ValueError(f"Could not read a host from URL: {url!r}")

    for suffix, source in _SUPPORTED_HOSTS.items():
        # Match the bare domain or any subdomain (e.g. www.udemy.com).
        if host == suffix or host.endswith("." + suffix):
            return source

    raise ValueError(
        f"Unsupported host {host!r}. Only Udemy and W3Schools URLs are supported."
    )
