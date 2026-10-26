def add(a, b):
    """Return the sum of a and b.

    Args:
        a (int or float): First addend.
        b (int or float): Second addend.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b


def divide(a, b):
    """Return the division of a by b as a float.

    Args:
        a (int or float): Numerator.
        b (int or float): Denominator.

    Raises:
        ValueError: If b is zero.

    Returns:
        float: Result of a / b.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
