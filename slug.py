import re


def slugify(text: str) -> str:
    """Lowercase text, replace non-alphanumeric runs with hyphens, and strip hyphens."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text).lower()
    return slug.strip("-")
