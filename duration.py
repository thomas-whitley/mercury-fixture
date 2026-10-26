"""
Parse duration strings like "1h30m" into total seconds.
"""


def parse_duration(text: str) -> int:
    """Convert a duration string to seconds.

    The string may contain an integer followed by ``h``, ``m``, or ``s`` in that
    order, each component at most once and without spaces. At least one
    component must be present.

    Raises:
        ValueError: If the format is invalid.
    """
    import re

    if not isinstance(text, str):
        raise ValueError("duration must be a string")

    # Pattern allows optional hours, then optional minutes, then optional seconds.
    pattern = re.compile(r'^(?:(?P<h>\d+)h)?(?:(?P<m>\d+)m)?(?:(?P<s>\d+)s)?$')
    match = pattern.fullmatch(text)
    if not match:
        raise ValueError(f"Invalid duration format: {text!r}")

    # Ensure at least one component is present.
    if not any(match.group(name) is not None for name in ("h", "m", "s")):
        raise ValueError("Empty duration string")

    hours = int(match.group('h')) if match.group('h') is not None else 0
    minutes = int(match.group('m')) if match.group('m') is not None else 0
    seconds = int(match.group('s')) if match.group('s') is not None else 0
    return hours * 3600 + minutes * 60 + seconds
