import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class ClampTest(unittest.TestCase):
    def test_within_range(self):
        self.assertEqual(clamp(5, 1, 10), 5)

    def test_below_low(self):
        self.assertEqual(clamp(-1, 0, 5), 0)

    def test_above_high(self):
        self.assertEqual(clamp(10, 0, 5), 5)

    def test_low_greater_than_high_raises(self):
        with self.assertRaises(ValueError):
            clamp(3, 10, 5)


if __name__ == "__main__":
    unittest.main()
