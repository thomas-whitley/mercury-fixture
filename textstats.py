"""Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix."""

from collections import Counter


def word_count(text: str) -> int:
    return len(text.split(" "))


def most_common(text: str, n: int) -> list[tuple[str, int]]:
    if n < 1:
        raise ValueError("n must be at least 1")
    
    words = text.split()
    lowercased_words = [w.lower() for w in words]
    
    counts = Counter(lowercased_words)
    
    # Sort by count descending, then word alphabetically ascending
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_items[:n]
