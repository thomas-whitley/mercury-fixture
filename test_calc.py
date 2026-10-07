import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_cli_add_success(self):
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "5\n")
        self.assertEqual(result.stderr, "")

    def test_cli_wrong_command(self):
        result = subprocess.run(
            [sys.executable, "-m", "calc", "sub", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")

    def test_cli_wrong_arg_count(self):
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")

    def test_cli_non_integer_arg(self):
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "a", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
