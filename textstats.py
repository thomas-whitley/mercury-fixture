def char_count(s: str) -> int:
    """Return the number of characters in the string `s`."""
    return len(s)


def line_count(s: str) -> int:
    """Return the number of lines in the string `s`.

    An empty string has 0 lines. Lines are separated by the newline character ``'\n'``.
    """
    if not s:
        return 0
    # Count the number of newline characters and add one for the last line
    return s.count('\n') + 1


def word_count(s: str) -> int:
    """Return the number of whitespace‑separated words in the string `s`.

    Words are delimited by any whitespace characters (spaces, tabs, newlines, etc.).
    Consecutive whitespace is treated as a single separator and leading/trailing
    whitespace is ignored. An empty string results in a count of ``0``.
    """
    # ``str.split()`` without arguments splits on arbitrary runs of whitespace
    # and returns an empty list for an empty string, which gives the correct count.
    return len(s.split())


__all__ = ["char_count", "line_count", "word_count"]
