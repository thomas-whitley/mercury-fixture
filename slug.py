import re

def slugify(text: str) -> str:
    """Return a URL‑friendly slug.

    The function lower‑cases the input, replaces any run of characters that are
    not ASCII letters or digits with a single hyphen, and removes leading and
    trailing hyphens. An empty input returns an empty string.
    """
    # Lower‑case the text
    lowered = text.lower()
    # Replace non‑alphanumeric runs with a hyphen
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    # Strip hyphens from both ends
    return slug.strip("-")
