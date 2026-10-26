# test_calc_cli.py
"""CLI tests for the ``calc`` module.

These tests verify that the module can be executed with ``python -m calc`` and
behaves according to the specification:

* ``add A B`` prints the sum and exits with status ``0``.
* Any misuse results in an error message on *stderr* and exit status ``2``.
"""

import unittest
import subprocess
import sys


class TestCalcCLI(unittest.TestCase):
    def _run_calc(self, *args: str) -> subprocess.CompletedProcess:
        """Run ``python -m calc`` with the supplied arguments.

        Returns the :class:`subprocess.CompletedProcess` so the caller can
        inspect ``returncode``, ``stdout`` and ``stderr``.
        """
        cmd = [sys.executable, "-m", "calc"] + list(args)
        return subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_success(self):
        """Valid invocation should print the sum and exit with status 0."""
        result = self._run_calc("add", "2", "3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "5")
        self.assertEqual(result.stderr, "")

    def test_cli_missing_arguments(self):
        """Too few arguments must result in exit status 2 and a usage message."""
        result = self._run_calc("add", "2")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage", result.stderr)

    def test_cli_invalid_command(self):
        """Any command other than ``add`` is treated as invalid."""
        result = self._run_calc("multiply", "2", "3")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage", result.stderr)

    def test_cli_non_integer_arguments(self):
        """Non‑integer arguments must cause an error with status 2."""
        result = self._run_calc("add", "a", "b")
        self.assertEqual(result.returncode, 2)
        self.assertIn("integers", result.stderr.lower())

if __name__ == "__main__":
    unittest.main()
