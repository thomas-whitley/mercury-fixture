import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_clamp_values(self):
        self.assertEqual(clamp(1, 2, 3), 2)
        self.assertEqual(clamp(4, 2, 3), 3)
        self.assertEqual(clamp(2, 2, 2), 2)

    def test_clamp_low_greater_than_high(self):
        with self.assertRaises(ValueError):
            clamp(1, 3, 2)