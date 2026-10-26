"""
calc module provides an ``add`` function and a simple command line interface.

Usage:
    python -m calc add A B
"""


def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    The function is deliberately tiny so that it can be imported by other
    modules (e.g. the test suite) without side‑effects.
    """
    return a + b


def _main() -> None:
    import sys
    args = sys.argv[1:]
    # Expected pattern: add A B
    if len(args) != 3 or args[0] != "add":
        sys.stderr.write("Usage: python -m calc add A B\n")
        sys.exit(2)
    _, a_str, b_str = args
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        sys.stderr.write("Both A and B must be integers.\n")
        sys.exit(2)
    # Successful execution – print the sum and exit with status 0.
    print(add(a, b))
    sys.exit(0)


if __name__ == "__main__":
    _main()
