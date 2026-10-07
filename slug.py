import re

def slugify(text: str) -> str:
    """Return a slugified version of *text*.

    The algorithm lower‑cases the input, replaces any run of characters that are
    not ASCII letters (a‑z) or digits (0‑9) with a single hyphen, and then strips
    hyphens from both the start and end of the result. If the final string would
    be empty, an empty string is returned.
    """
    # Lower‑case the text first.
    lowered = text.lower()
    # Replace runs of non‑ASCII‑alphanumerics with a hyphen.
    # The pattern matches one or more characters that are NOT a‑z or 0‑9.
    replaced = re.sub(r"[^a-z0-9]+", "-", lowered)
    # Strip hyphens from both ends.
    slug = replaced.strip("-")
    return slug
