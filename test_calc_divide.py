import unittest

from calc import divide


class DivideTest(unittest.TestCase):
    def test_divide_normal(self):
        result = divide(7, 2)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as cm:
            divide(10, 0)
        self.assertEqual(str(cm.exception), "cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
