# calc.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return the division of a by b as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
