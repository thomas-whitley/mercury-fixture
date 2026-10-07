import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_clamp_below_low(self):
        self.assertEqual(clamp(-1, 0, 5), 0)

    def test_clamp_above_high(self):
        self.assertEqual(clamp(6, 0, 5), 5)

    def test_clamp_within_range(self):
        self.assertEqual(clamp(3, 0, 5), 3)

    def test_clamp_low_high_swap_raises_error(self):
        with self.assertRaises(ValueError):
            clamp(3, 5, 0)


if __name__ == "__main__":
    unittest.main()