import unittest
import pytest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


def test_divide_normal():
    result = divide(10, 2)
    assert isinstance(result, float)
    assert result == 5.0


def test_divide_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert str(exc_info.value) == "cannot divide by zero"


if __name__ == "__main__":
    unittest.main()
