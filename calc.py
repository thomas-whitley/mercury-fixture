"""A deliberately small module for Mercury's repo chore integration test to edit."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    """Return a / b as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
