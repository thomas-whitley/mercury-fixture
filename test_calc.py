import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_cli_add(self):
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "5\n")
        self.assertEqual(result.stderr, "")

    def test_cli_invalid_args(self):
        # Wrong number of arguments
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "2"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)

        # Non-integer arguments
        result = subprocess.run(
            [sys.executable, "-m", "calc", "add", "a", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)

        # Unknown command
        result = subprocess.run(
            [sys.executable, "-m", "calc", "sub", "2", "3"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
