import unittest

from calc import add, subtract


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class SubtractTest(unittest.TestCase):
    def test_subtracts_two_numbers(self):
        self.assertEqual(subtract(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
