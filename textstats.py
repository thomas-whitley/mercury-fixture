'''textstats module

Provides simple text statistics functions.
'''

def word_count(text: str) -> int:
    """Return the number of whitespace‑separated words in *text*.

    The function uses the default ``str.split()`` behaviour which splits on any
    whitespace (spaces, tabs, newlines, etc.) and discards empty strings. This
    correctly handles multiple consecutive whitespace characters and returns
    ``0`` for an empty string.

    Parameters
    ----------
    text: str
        The string to be analysed.

    Returns
    -------
    int
        Number of words found.
    """
    if not isinstance(text, str):
        raise TypeError("word_count expects a string")
    # ``split()`` without arguments splits on any whitespace and omits empty parts.
    return len(text.split())
