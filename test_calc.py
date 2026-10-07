import unittest
import subprocess
import sys

import pytest

from calc import add


class AddTest(unittest.TestCase):
    def test_adds_two_numbers(self):
        self.assertEqual(add(2, 3), 5)


def _run(args):
    """Helper that runs ``python -m calc`` with the supplied *args*.

    Returns the CompletedProcess instance.
    """
    return subprocess.run(
        [sys.executable, "-m", "calc"] + args,
        capture_output=True,
        text=True,
    )


def test_cli_success():
    result = _run(["add", "2", "3"]) 
    assert result.returncode == 0
    assert result.stdout.strip() == "5"
    assert result.stderr == ""


def test_cli_missing_arguments():
    result = _run(["add", "2"])  # only one operand provided
    assert result.returncode == 2
    assert result.stderr != ""


def test_cli_non_integer():
    result = _run(["add", "foo", "1"])  # non‑integer argument
    assert result.returncode == 2
    assert result.stderr != ""
