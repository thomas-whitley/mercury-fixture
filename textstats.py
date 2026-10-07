"""Text statistics for Mercury's evals. word_count has a known bug the evals ask a model to fix."""


def word_count(text: str) -> int:
    if not text or not text.strip():
        return 0
    return len(text.split())
