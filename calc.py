"""A deliberately small module for Mercury's repo chore integration test to edit."""


def add(a: int, b: int) -> int:
    return a + b


def clamp(value: float, low: float, high: float) -> float:
    """Clamp value to the range [low, high].

    Args:
        value: The value to clamp.
        low: The lower bound (inclusive).
        high: The upper bound (inclusive).

    Returns:
        low if value < low, high if value > high, otherwise value.

    Raises:
        ValueError: If low > high.
    """
    if low > high:
        raise ValueError("low must not be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
