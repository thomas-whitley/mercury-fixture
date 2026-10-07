# textstats module provides utilities for textual analysis.
#
# Currently implements:
# - word_count(text): Return the number of whitespace‑separated words (case‑insensitive).
# - most_common(text, n): Return the n most frequent words in the given text.
#
# Words are whitespace separated and compared lowercased. Ordering for most_common is by count
# descending and alphabetically for ties.

from collections import Counter
from typing import List, Tuple


def word_count(text: str) -> int:
    """Return the count of words in *text*.

    The text is split on any whitespace. Comparison is case‑insensitive, but the
    count only reflects the total number of whitespace‑separated tokens.
    An empty string yields ``0``.

    Parameters
    ----------
    text:
        The input string to analyse.

    Returns
    -------
    int
        Number of words in the given text.
    """
    # Split on any whitespace; an empty string results in an empty list.
    words = text.split()
    return len(words)


def most_common(text: str, n: int) -> List[Tuple[str, int]]:
    """Return a list of the *n* most frequent words in *text*.

    Words are defined as sequences of characters separated by any whitespace.
    Comparison is case‑insensitive: all words are lower‑cased before counting.

    The result is a list of ``(word, count)`` tuples ordered by descending
    frequency.  Ties are broken alphabetically (ascending).  If *n* exceeds the
    number of distinct words, all words are returned.

    Parameters
    ----------
    text:
        The input string to analyse.
    n:
        Number of top entries to return.  Must be a positive integer.

    Returns
    -------
    List[Tuple[str, int]]
        The most common words and their frequencies.

    Raises
    ------
    ValueError
        If *n* is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Obtain word frequencies (case‑insensitive)
    counts = Counter(word.lower() for word in text.split())

    if not counts:
        return []

    # Sort by count descending then alphabetically ascending
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    # Slice to the requested number of items (or all if fewer)
    return sorted_items[:n]
