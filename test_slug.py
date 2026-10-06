import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_special_characters(self):
        self.assertEqual(slugify("   foo--bar! 123?   "), "foo-bar-123")

    def test_unicode_and_punctuation(self):
        self.assertEqual(slugify("Café résumé, 100%!"), "caf-r-sum-100")


if __name__ == "__main__":
    unittest.main()
