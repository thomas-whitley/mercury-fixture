'''Roman numeral conversion.

Provides a single function `to_roman` that converts an integer in the range
1‑3999 (inclusive) to its Roman numeral representation using standard
subtractive notation.

If the value is outside the allowed range a `ValueError` is raised.
'''

def to_roman(n: int) -> str:
    """Return the Roman numeral representation of *n*.

    Args:
        n: An integer between 1 and 3999 inclusive.

    Returns:
        A string containing the Roman numeral.

    Raises:
        ValueError: If *n* is not in the allowed range.
    """
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError("Roman numerals only support integers from 1 to 3999")

    # Mapping of integer values to Roman numerals, ordered from largest to smallest.
    numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, symbol in numerals:
        while n >= value:
            result.append(symbol)
            n -= value
        if n == 0:
            break
    return "".join(result)
