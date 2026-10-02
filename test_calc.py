import unittest

from calc import add, multiply


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class MultiplyTest(unittest.TestCase):
    def test_multiplies_two_numbers(self):
        self.assertEqual(multiply(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
