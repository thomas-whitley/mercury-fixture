import unittest

from calc import add, clamp


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class ClampTest(unittest.TestCase):
    def test_value_below_low_returns_low(self):
        self.assertEqual(clamp(0, 5, 10), 5)
        self.assertEqual(clamp(-3, -2, 2), -2)

    def test_value_above_high_returns_high(self):
        self.assertEqual(clamp(15, 5, 10), 10)
        self.assertEqual(clamp(5, -2, 2), 2)

    def test_value_within_range_returns_value(self):
        self.assertEqual(clamp(7, 5, 10), 7)
        self.assertEqual(clamp(0, -2, 2), 0)
        self.assertEqual(clamp(5, 5, 10), 5)  # at low bound
        self.assertEqual(clamp(10, 5, 10), 10)  # at high bound

    def test_low_greater_than_high_raises_value_error(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 5)
        with self.assertRaises(ValueError):
            clamp(0, 1, 0)

    def test_works_with_floats(self):
        self.assertAlmostEqual(clamp(3.14, 0.0, 5.0), 3.14)
        self.assertAlmostEqual(clamp(-1.5, 0.0, 5.0), 0.0)
        self.assertAlmostEqual(clamp(6.0, 0.0, 5.0), 5.0)


if __name__ == "__main__":
    unittest.main()
