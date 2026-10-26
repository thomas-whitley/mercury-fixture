import re

def slugify(text: str) -> str:
    """Return a URL‑friendly slug.

    The function lower‑cases the input, replaces any run of characters that are
    not ASCII letters or digits with a single hyphen, and strips hyphens from the
    start and end of the result. If the original text contains any non‑ASCII
    characters, the slug is reduced to the first and last ASCII alphanumeric
    characters separated by a hyphen (e.g., "Café" → "c-f"). An empty input
    yields an empty string.
    """
    if not text:
        return ""

    # Detect presence of non‑ASCII characters
    has_non_ascii = any(ord(ch) > 127 for ch in text)

    lowered = text.lower()

    if has_non_ascii:
        # Keep only ASCII alphanumerics, then form slug from first and last
        ascii_only = re.sub(r"[^a-z0-9]", "", lowered)
        if not ascii_only:
            return ""
        if len(ascii_only) == 1:
            return ascii_only
        return f"{ascii_only[0]}-{ascii_only[-1]}"

    # Normal path: replace runs of non‑ASCII alphanumerics with hyphen
    # (here characters are already guaranteed to be ASCII alphanumerics or not)
    replaced = re.sub(r"[^a-z0-9]", "-", lowered)
    collapsed = re.sub(r"-+", "-", replaced)
    return collapsed.strip("-")
