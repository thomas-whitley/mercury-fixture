import unittest

from calc import add, clamp

class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

class ClampTest(unittest.TestCase):
    def test_clamp_within_range(self):
        self.assertEqual(clamp(5, 3, 7), 5)

    def test_clamp_below_range(self):
        self.assertEqual(clamp(1, 3, 7), 3)

    def test_clamp_above_range(self):
        self.assertEqual(clamp(8, 3, 7), 7)

    def test_clamp_raises_exception_on_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 7, 3)

if __name__ == "__main__":
    unittest.main()