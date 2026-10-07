def add(a, b):
    """Return the sum of *a* and *b*."""
    return a + b


def clamp(value, low, high):
    """Clamp *value* to the inclusive range defined by *low* and *high*.

    Returns ``low`` if ``value`` is less than ``low``, ``high`` if ``value`` is greater
    than ``high``, and ``value`` otherwise.  If ``low`` is greater than ``high`` a
    :class:`ValueError` is raised.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
