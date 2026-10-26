def to_roman(n: int) -> str:
    """Return the Roman numeral representation of an integer between 1 and 3999."""
    if not isinstance(n, int) or not (1 <= n <= 3999):
        raise ValueError("n must be an integer between 1 and 3999")

    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = []
    for value, symbol in roman_numerals:
        while n >= value:
            result.append(symbol)
            n -= value
    return ''.join(result)
