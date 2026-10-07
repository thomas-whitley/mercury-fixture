# Utility functions for text statistics.

"""
Utility functions for text statistics.
"""

from collections import Counter
from typing import List, Tuple


def word_count(text: str) -> int:
    """Return the number of words in *text*.

    Words are defined as whitespace‑separated tokens. The function simply
    splits the string on any whitespace and returns the length of the resulting
    list. Empty strings result in a count of ``0``.

    Parameters
    ----------
    text: str
        The input text.

    Returns
    -------
    int
        The number of words.
    """
    # ``str.split`` without arguments splits on any consecutive whitespace.
    # It also discards leading/trailing whitespace, which matches the expected
    # behaviour for counting words.
    return len(text.split())


def most_common(text: str, n: int) -> List[Tuple[str, int]]:
    """Return a list of the *n* most frequent words in *text*.

    Words are defined as whitespace‑separated tokens and are compared
    case‑insensitively (lower‑cased). The returned list is ordered by
    decreasing frequency; words with the same frequency are ordered
    alphabetically.

    Parameters
    ----------
    text: str
        The input text.
    n: int
        Number of most common words to return. Must be >= 1.

    Returns
    -------
    List[Tuple[str, int]]
        List of ``(word, count)`` tuples.

    Raises
    ------
    ValueError
        If *n* is less than 1.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    # Split on any whitespace, lower‑case each word
    words = [w.lower() for w in text.split()]

    # Count occurrences
    counter = Counter(words)

    # Sort by count descending, then word ascending (alphabetical)
    sorted_items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

    # Return up to n items
    return sorted_items[:n]
