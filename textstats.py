"""Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix."""

def word_count(text: str) -> int:
    """Return the number of words separated by any whitespace.

    Empty strings return 0.
    """
    # Using str.split() without arguments splits on any whitespace (spaces, tabs, newlines, etc.)
    # and discards empty strings, which gives the correct count.
    return len(text.split())
