import unittest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class DivideTest(unittest.TestCase):
    def test_divides_two_numbers(self):
        self.assertEqual(divide(6, 2), 3.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(10, 4), 2.5)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            divide(5, 0)
        self.assertEqual(str(cm.exception), "cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
