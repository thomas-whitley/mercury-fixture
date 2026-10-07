def clamp(value, low, high):
    """Return *low* if *value* is below *low*, *high* if above *high*, otherwise *value*.

    Raises:
        ValueError: If ``low`` is greater than ``high``.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
