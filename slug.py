import re


def slugify(text: str) -> str:
    """Return a URL‑friendly slug for *text*.

    The function lower‑cases the input, replaces each run of characters that are
    not ASCII letters (a‑z) or digits (0‑9) with a single hyphen, and strips any
    hyphens from the start and end of the result. If the result is empty, an empty
    string is returned.
    """
    if not text:
        return ""
    # Lower‑case and replace non‑ASCII‑alnum runs with a hyphen
    lowered = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    # Strip leading/trailing hyphens
    return slug.strip("-")
