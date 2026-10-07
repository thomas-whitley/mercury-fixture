def add(a, b):
    """Return the sum of *a* and *b*.

    This function is part of the original repository and is used by the
    existing tests.
    """
    return a + b


def divide(a, b):
    """Return *a* divided by *b* as a float.

    Raises:
        ValueError: If ``b`` is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
