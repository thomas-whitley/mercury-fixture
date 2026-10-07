import re


def slugify(text: str) -> str:
    """Lowercase text, replace non-ASCII letters/digits runs with a hyphen, and strip hyphens."""
    lowered = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-")
