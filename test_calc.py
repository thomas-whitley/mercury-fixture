import unittest
import subprocess
import sys

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


class CLITest(unittest.TestCase):
    def run_calc(self, args):
        """Run python -m calc with given args, return (returncode, stdout, stderr)."""
        cmd = [sys.executable, "-m", "calc"] + args
        proc = subprocess.run(cmd, capture_output=True, text=True)
        return proc.returncode, proc.stdout, proc.stderr

    def test_add_command_success(self):
        code, out, err = self.run_calc(["add", "2", "3"])
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "5")
        self.assertEqual(err, "")

    def test_add_command_wrong_number_of_args(self):
        code, out, err = self.run_calc(["add", "2"])
        self.assertEqual(code, 2)
        self.assertIn("Usage", err)
        self.assertEqual(out, "")

    def test_add_command_non_integer_args(self):
        code, out, err = self.run_calc(["add", "2", "x"])
        self.assertEqual(code, 2)
        self.assertIn("Arguments must be integers", err)
        self.assertEqual(out, "")

    def test_unknown_command(self):
        code, out, err = self.run_calc(["sub", "2", "3"])
        self.assertEqual(code, 2)
        self.assertIn("Unknown command", err)
        self.assertEqual(out, "")

    def test_no_command(self):
        code, out, err = self.run_calc([])
        self.assertEqual(code, 2)
        self.assertIn("Usage", err)
        self.assertEqual(out, "")


if __name__ == "__main__":
    unittest.main()
