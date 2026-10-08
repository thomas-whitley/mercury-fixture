import unittest

from calc import add, divide


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class DivideTest(unittest.TestCase):
    def test_divides_two_numbers(self):
        self.assertEqual(divide(6, 3), 2.0)


if __name__ == "__main__":
    unittest.main()
