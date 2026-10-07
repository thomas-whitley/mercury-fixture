'''Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix.'''


def word_count(text: str) -> int:
    return len(text.split(' '))

from collections import Counter
from typing import List, Tuple


def most_common(text: str, n: int) -> List[Tuple[str, int]]:
    """Return a list of the *n* most frequent words as ``(word, count)`` tuples.

    Words are split on any whitespace and compared case‑insensitively.
    The result is ordered by descending frequency; ties are broken
    alphabetically. If ``n`` is less than ``1`` a :class:`ValueError` is raised.
    """
    if n < 1:
        raise ValueError('n must be at least 1')

    # Normalise words to lower‑case and split on any whitespace.
    words = [w.lower() for w in text.split()]
    counter = Counter(words)

    # Sort first by descending count then alphabetically.
    sorted_items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]
