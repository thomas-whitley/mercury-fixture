import unittest
import pytest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    assert str(excinfo.value) == "cannot divide by zero"


if __name__ == "__main__":
    unittest.main()
