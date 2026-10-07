def to_roman(n):
    if not 1 <= n <= 3999:
        raise ValueError
    roman_numeral = ''
    value_map = (
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    
    for value, numeral in value_map:
        while n >= value:
            roman_numeral += numeral
            n -= value
    return roman_numeral

def test_to_roman():
    assert to_roman(1) == 'I'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(9) == 'IX'
    assert to_roman(10) == 'X'
    assert to_roman(40) == 'XL'
    assert to_roman(90) == 'XC'
    assert to_roman(100) == 'C'
    assert to_roman(400) == 'CD'
    assert to_roman(900) == 'CM'
    assert to_roman(3999) == 'MMMCMXCIX'