'''Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix.'''

def word_count(text: str) -> int:
    """Return the number of words in *text* separated by any whitespace.

    Consecutive whitespace characters are treated as a single separator and
    leading/trailing whitespace is ignored. An empty string yields 0.
    """
    return len(text.split())
