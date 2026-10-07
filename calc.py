'''A deliberately small module for Mercury's repo chore integration test to edit.'''


def add(a: int, b: int) -> int:
    return a + b


def clamp(value: int, low: int, high: int) -> int:
    """Return *low* if *value* is below *low*, *high* if *value* is above *high*,
    otherwise return *value*.

    Raises:
        ValueError: If *low* is greater than *high*.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
