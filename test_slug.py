import unittest

from slug import slugify


class SlugTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_special_characters_and_spaces(self):
        self.assertEqual(slugify("   Foo  Bar---Baz! "), "foo-bar-baz")

    def test_digits(self):
        self.assertEqual(slugify("Version 2.0 Release!"), "version-2-0-release")


if __name__ == "__main__":
    unittest.main()
