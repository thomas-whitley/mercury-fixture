def add(a, b):
    """Return the sum of *a* and *b*."""
    return a + b


def clamp(value, low, high):
    """Return *value* clamped to the inclusive range [low, high].

    If *low* is greater than *high*, a ``ValueError`` is raised.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
