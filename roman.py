def to_roman(n: int) -> str:
    """Return the Roman numeral representation of ``n``.

    ``n`` must be an integer between 1 and 3999 inclusive.  Values outside that
    range raise ``ValueError``.
    """
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError("Argument must be an integer between 1 and 3999 inclusive")

    # Mapping of integer values to Roman numerals, ordered from largest to
    # smallest.  Subtractive forms are included directly.
    roman_numerals = [
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
    for value, numeral in roman_numerals:
        while n >= value:
            result.append(numeral)
            n -= value
        if n == 0:
            break
    return "".join(result)
