"""A deliberately small module for Mercury's repo chore integration test to edit."""


def add(a: int, b: int) -> int:
    return a + b


def clamp(value, low, high):
    if low > high:
        raise ValueError("low cannot be greater than high")
    if value < low:
        return low
    if value > high:
        return high
    return value
