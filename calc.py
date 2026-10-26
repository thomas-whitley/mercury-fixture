# calc.py
"""Simple calculator module.

Provides an :func:`add` function and a command‑line interface that can be
invoked as ``python -m calc add A B``.

The CLI prints the sum of ``A`` and ``B`` (both integers) followed by a newline
and exits with status ``0``.  Any misuse – wrong command, wrong number of
arguments, or non‑integer arguments – results in an error message on *stderr*
and an exit status of ``2``.
"""

from __future__ import annotations

def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    This function is deliberately tiny so that it can be imported and used in
    other code without pulling in the command‑line handling machinery.
    """
    return a + b


def _main() -> None:
    """Entry‑point for ``python -m calc``.

    Expected usage::

        python -m calc add A B

    where ``A`` and ``B`` are integers.
    """
    import sys

    # Expected: script name, the literal command "add", and two integer args.
    if len(sys.argv) != 4 or sys.argv[1] != "add":
        sys.stderr.write("Usage: python -m calc add A B\n")
        sys.exit(2)

    try:
        a = int(sys.argv[2])
        b = int(sys.argv[3])
    except ValueError:
        sys.stderr.write("Both A and B must be integers\n")
        sys.exit(2)

    result = add(a, b)
    # ``print`` adds its own newline, satisfying the requirement.
    print(result)
    sys.exit(0)


if __name__ == "__main__":
    _main()
