'''Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix.'''


def word_count(text: str) -> int:
    """Return the number of words in *text* separated by any whitespace.

    Uses the default ``str.split`` behaviour which splits on runs of
    whitespace characters (space, tab, newline, etc.) and discards empty
    strings, so an empty input returns ``0``.
    """
    return len(text.split())
