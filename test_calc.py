import unittest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class DivideTest(unittest.TestCase):
    def test_divides_by_two(self):
        self.assertEqual(divide(4, 2), 2.0)

    def test_divides_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(4, 0)
        self.assertIn('cannot divide by zero', str(context.exception))


if __name__ == "__main__":
    unittest.main()