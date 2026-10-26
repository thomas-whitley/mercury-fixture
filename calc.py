"""A deliberately small module for Mercury's repo chore integration test to edit."""

import sys


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m calc add A B", file=sys.stderr)
        sys.exit(2)
    command = sys.argv[1]
    if command != "add":
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(2)
    if len(sys.argv) != 4:
        print("Usage: python -m calc add A B", file=sys.stderr)
        sys.exit(2)
    try:
        a = int(sys.argv[2])
        b = int(sys.argv[3])
    except ValueError:
        print("Arguments must be integers", file=sys.stderr)
        sys.exit(2)
    result = add(a, b)
    print(result)
    sys.exit(0)
