import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_non_alnum(self):
        self.assertEqual(slugify("Multiple---___---Separators"), "multiple-separators")

    def test_surrounding_hyphens(self):
        self.assertEqual(slugify("---Hello---"), "hello")


if __name__ == "__main__":
    unittest.main()
