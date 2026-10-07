'''Utility to convert integers to Roman numerals.'''

def to_roman(n: int) -> str:
    """Return the Roman numeral representation of *n*.

    *n* must be an integer between 1 and 3999 inclusive. Otherwise a
    :class:`ValueError` is raised.
    """
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError("n must be an integer between 1 and 3999")

    # Mapping of Roman numerals in descending order, including subtractive forms.
    roman_map = [
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
    for value, numeral in roman_map:
        while n >= value:
            result.append(numeral)
            n -= value
    return "".join(result)
