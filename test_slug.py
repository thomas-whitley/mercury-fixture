import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty(self):
        self.assertEqual(slugify(""), "")

    def test_multiple_non_alnum(self):
        self.assertEqual(slugify("foo@@@bar---baz"), "foo-bar-baz")

    def test_leading_and_trailing(self):
        self.assertEqual(slugify("---Hello---"), "hello")

    def test_spaces_and_unicode(self):
        # Spaces become hyphens, non‑ASCII letters are treated as non‑alnum.
        self.assertEqual(slugify("  Café au lait  "), "caf-au-lait")

    def test_all_non_alnum(self):
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
