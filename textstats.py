import collections

__all__ = ["most_common", "word_count"]

def most_common(text: str, n: int):
    """Return a list of the *n* most frequent words in *text*.

    Words are separated by whitespace and compared in lower‑case.
    The result is a list of ``(word, count)`` tuples ordered by descending
    count and, for equal counts, alphabetically.

    Args:
        text: The input string.
        n: Number of top items to return. Must be ``>= 1``.

    Returns:
        A list of ``(word, count)`` tuples.

    Raises:
        ValueError: If ``n`` is less than 1.
    """
    if n < 1:
        raise ValueError("n must be at least 1")

    # Split on any whitespace and normalise to lower case
    words = (w.lower() for w in text.split())
    counter = collections.Counter(words)

    # Sort by count descending, then alphabetically
    sorted_items = sorted(
        counter.items(),
        key=lambda item: (-item[1], item[0])
    )

    # Return the first n items (or all if fewer exist)
    return sorted_items[:n]

def word_count(text: str) -> int:
    """Return the number of whitespace‑separated words in *text*.

    The function simply splits the string on any whitespace and returns the
    length of the resulting list.
    """
    # ``str.split`` without arguments splits on any whitespace and discards
    # empty strings, which matches the behaviour expected by the original test.
    return len(text.split())
