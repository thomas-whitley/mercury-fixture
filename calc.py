"""A deliberately small module for Mercury's repo chore integration test to edit."""


def add(a: int, b: int) -> int:
    return a + b


def _run_cli() -> None:
    import sys
    args = sys.argv[1:]
    # Expected: add A B
    if len(args) != 3 or args[0] != "add":
        print("Invalid usage: expected 'add A B'", file=sys.stderr)
        sys.exit(2)
    _, a_str, b_str = args[0], args[1], args[2]
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        print("Both A and B must be integers", file=sys.stderr)
        sys.exit(2)
    result = add(a, b)
    print(result)
    sys.exit(0)


if __name__ == "__main__":
    _run_cli()
