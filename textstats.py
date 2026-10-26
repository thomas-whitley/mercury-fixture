'''Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix.'''

from collections import Counter


def word_count(text: str) -> int:
    return len(text.split(" "))


def most_common(text: str, n: int) -> list[tuple[str, int]]:
    """Return a list of the *n* most frequent words in *text*.

    Words are separated by any whitespace and compared case‑insensitively
    (lower‑cased). The result is a list of ``(word, count)`` tuples ordered
    by descending count and then alphabetically for ties. If ``n`` is less
    than ``1`` a :class:`ValueError` is raised. If ``n`` exceeds the number of
    distinct words, all words are returned.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    # Split on any whitespace, lower‑case each word
    words = [w.lower() for w in text.split() if w]
    counts = Counter(words)

    # Sort by count descending then alphabetically ascending
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]
