import unittest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class DivideTest(unittest.TestCase):
    def test_divides_two_numbers(self):
        self.assertEqual(divide(6, 3), 2.0)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ctx:
            divide(5, 0)
        self.assertEqual(str(ctx.exception), "cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
