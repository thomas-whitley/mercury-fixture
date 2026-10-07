# test_calc.py
import pytest
import calc

# Existing tests (if any) would be here

def test_divide():
    result = calc.divide(10, 2)
    assert result == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        calc.divide(1, 0)
    assert str(excinfo.value) == "cannot divide by zero"
