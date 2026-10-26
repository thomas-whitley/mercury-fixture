import unittest

from calc import add, clamp

class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

class TestClamp(unittest.TestCase):
    def test_value_below_low(self):
        self.assertEqual(clamp(-5, 0, 10), 0)
        self.assertEqual(clamp(2, 5, 10), 5)

    def test_value_above_high(self):
        self.assertEqual(clamp(15, 0, 10), 10)
        self.assertEqual(clamp(100, 20, 30), 30)

    def test_value_within_range(self):
        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(20, 10, 30), 20)
        self.assertEqual(clamp(0, 0, 0), 0)

    def test_low_equals_high(self):
        # When low == high, the only allowed value is that exact number
        self.assertEqual(clamp(5, 5, 5), 5)
        self.assertEqual(clamp(0, 5, 5), 5)
        self.assertEqual(clamp(10, 5, 5), 5)

    def test_invalid_range_raises(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)
        with self.assertRaises(ValueError):
            clamp(0, 1, -1)

if __name__ == "__main__":
    unittest.main()
