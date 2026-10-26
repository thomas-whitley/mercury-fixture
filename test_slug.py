import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_separators(self):
        self.assertEqual(
            slugify("  Multiple   spaces---and___underscores!!"),
            "multiple-spaces-and-underscores",
        )

    def test_leading_and_trailing_hyphens(self):
        self.assertEqual(slugify("-Hello-"), "hello")

    def test_non_ascii_characters(self):
        # "é" is not an ASCII letter, so it becomes a separator, yielding a hyphen
        self.assertEqual(slugify("Café"), "c-f")


if __name__ == "__main__":
    unittest.main()
