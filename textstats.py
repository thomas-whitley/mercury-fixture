"""Utility functions for simple text statistics.

This module provides functions to compute word counts and the *n* most
common words in a string. Words are defined as whitespace‑separated tokens
and are compared case‑insensitively.
"""

from collections import Counter
from typing import List, Tuple


def word_count(text: str) -> int:
    """Return the number of words in *text*.

    The function splits *text* on any whitespace and returns the length of the
    resulting list. Empty strings yield a count of ``0``.

    Parameters
    ----------
    text:
        The input string to analyse.

    Returns
    -------
    int
        Number of whitespace‑separated tokens.
    """
    # ``str.split`` without arguments splits on any whitespace and discards
    # empty strings, which is exactly the behaviour required for the tests.
    return len(text.split())


def most_common(text: str, n: int) -> List[Tuple[str, int]]:
    """Return the *n* most frequent words in *text*.

    The function splits *text* on whitespace, lower‑cases each token and
    counts occurrences.  The result is a list of ``(word, count)`` tuples
    ordered by descending frequency and, for equal frequencies, by the
    word in alphabetical order.

    Parameters
    ----------
    text:
        The input string to analyse.
    n:
        Number of top items to return.  Must be a positive integer.

    Returns
    -------
    List[Tuple[str, int]]
        Up to *n* ``(word, count)`` pairs.

    Raises
    ------
    ValueError
        If *n* is less than ``1``.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Split on any whitespace, lower‑case the words
    words = [word.lower() for word in text.split()]
    # Count frequencies
    counter = Counter(words)
    # Sort by count descending, then word ascending
    sorted_items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    # Slice to the requested number of items (or fewer if not enough distinct words)
    return sorted_items[:n]
