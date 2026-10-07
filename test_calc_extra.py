import pytest
from calc import divide


def test_divide_normal():
    assert divide(6, 3) == 2.0


def test_divide_by_zero():
    with pytest.raises(ValueError) as exc:
        divide(1, 0)
    assert str(exc.value) == "cannot divide by zero"
