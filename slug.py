import re

def slugify(text: str) -> str:
    """Return a slugified version of *text*.

    The function lowercases the input, replaces any run of characters that are
    not ASCII letters or digits with a single hyphen, and strips hyphens from the
    start and end of the result. An empty string yields an empty string.
    """
    # Lower‑case the text first
    lowered = text.lower()
    # Replace any sequence of non‑ASCII letters/digits with a hyphen
    # ASCII letters are a‑z and digits 0‑9.
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    # Strip leading/trailing hyphens
    return slug.strip("-")
