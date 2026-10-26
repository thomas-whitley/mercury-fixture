import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_non_alnum(self):
        self.assertEqual(slugify("Hello---World"), "hello-world")

    def test_leading_trailing_non_alnum(self):
        self.assertEqual(slugify("!!!Hello World???"), "hello-world")

    def test_only_non_alnum(self):
        self.assertEqual(slugify("!!!@#$%"), "")

    def test_numbers_and_letters(self):
        self.assertEqual(slugify("Test123"), "test123")

    def test_unicode_stripped(self):
        # Non-ASCII letters are treated as non-alnum and replaced
        self.assertEqual(slugify("café"), "caf")

    def test_single_char(self):
        self.assertEqual(slugify("A"), "a")

    def test_hyphens_not_doubled(self):
        self.assertEqual(slugify("a--b"), "a-b")


if __name__ == "__main__":
    unittest.main()
