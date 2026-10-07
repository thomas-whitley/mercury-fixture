def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a / b as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return float(a) / float(b)
