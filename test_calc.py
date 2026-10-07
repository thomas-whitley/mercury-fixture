import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class CalcCliTest(unittest.TestCase):
    def run_cli(self, args):
        return subprocess.run(
            [sys.executable, "-m", "calc"] + args,
            capture_output=True,
            text=True
        )

    def test_cli_add_success(self):
        result = self.run_cli(["add", "2", "3"])
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "5\n")
        self.assertEqual(result.stderr, "")

    def test_cli_wrong_command(self):
        result = self.run_cli(["sub", "2", "3"])
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")

    def test_cli_wrong_arg_count(self):
        result = self.run_cli(["add", "2"])
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")

    def test_cli_non_integer_arg(self):
        result = self.run_cli(["add", "2", "foo"])
        self.assertEqual(result.returncode, 2)
        self.assertNotEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
