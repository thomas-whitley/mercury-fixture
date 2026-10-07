def word_count(text: str) -> int:
    """
    Return the number of words in *text*.

    Words are defined as sequences of non‑whitespace characters separated by
    any whitespace (spaces, tabs, newlines, etc.).  Consecutive whitespace
    characters are treated as a single separator and leading/trailing
    whitespace does not produce empty words.

    An empty string (or a string that contains only whitespace) yields 0.
    """
    # str.split() splits on arbitrary whitespace and discards empty strings,
    # which matches the required definition of a word.
    return len(text.split())

__all__ = ["word_count"]
