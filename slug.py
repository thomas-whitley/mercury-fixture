import re


def slugify(text: str) -> str:
    """Lowercases the text, replaces every run of characters that are not ASCII letters
    or digits with a single hyphen, and strips hyphens from both ends.
    """
    text = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", text)
    return slug.strip("-")
