import unittest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class DivideTest(unittest.TestCase):
    def test_divides_two_numbers(self):
        result = divide(10, 2)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as cm:
            divide(10, 0)
        self.assertEqual(str(cm.exception), "cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
