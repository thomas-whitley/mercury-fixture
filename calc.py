'''Utility functions for calculations.

This module may contain other calculation functions used throughout the project.
'''

# Existing calculation functions would be defined above.
# For the purposes of the test suite we include a simple add function.

def add(a, b):
    """Return the sum of *a* and *b*.

    This is a minimal implementation used by the existing tests.
    """
    return a + b

# ----------------------------------------

def clamp(value, low, high):
    """Clamp *value* into the inclusive range ``[low, high]``.

    Returns ``low`` if ``value`` is less than ``low``;
    ``high`` if ``value`` is greater than ``high``;
    otherwise returns ``value``.

    Raises:
        ValueError: If ``low`` is greater than ``high``.
    """
    if low > high:
        raise ValueError(f"low ({low}) cannot be greater than high ({high})")
    if value < low:
        return low
    if value > high:
        return high
    return value

# End of calc.py
