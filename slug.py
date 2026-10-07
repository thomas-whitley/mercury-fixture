import re


def slugify(text: str) -> str:
    """Lowercase the text, replace every run of characters that are not
    ASCII letters or digits with a single hyphen, and strip hyphens from both ends.
    """
    # Replace any sequence of non-alphanumeric ASCII characters with a hyphen
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text)
    # Lowercase and strip leading/trailing hyphens
    return slug.lower().strip("-")
