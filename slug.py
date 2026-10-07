'''Utility to generate URL-friendly slugs.'''

import re


def slugify(text: str) -> str:
    """
    Convert *text* to a slug.

    The algorithm lower‑cases the input, replaces each maximal run of characters
    that are not ASCII letters or digits with a single hyphen, and strips any
    leading or trailing hyphens.

    Examples
    --------
    >>> slugify("Hello, World!")
    'hello-world'
    >>> slugify("")
    ''
    """
    if not text:
        return ""
    # Lower‑case the input.
    lowered = text.lower()
    # Replace runs of non‑ASCII alphanumerics with a hyphen.
    slug = re.sub(r'[^0-9a-zA-Z]+', '-', lowered)
    # Strip leading/trailing hyphens.
    slug = slug.strip('-')
    return slug
