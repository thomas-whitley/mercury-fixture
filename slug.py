import re


def slugify(text: str) -> str:
    """Convert text to a slug.

    Lowercases the text, replaces every run of non-ASCII-letter-or-digit
    characters with a single hyphen, and strips hyphens from both ends.
    """
    if not text:
        return ""
    # Lowercase
    text = text.lower()
    # Replace runs of non-ASCII letters/digits with a single hyphen
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Strip hyphens from both ends
    return text.strip('-')
