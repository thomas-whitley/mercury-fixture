"""Utility to parse duration strings into total seconds.

The format is a concatenation of integer values followed by a unit letter:
    h – hours
    m – minutes
    s – seconds
Each unit may appear at most once and must appear in the order h, m, s.
No spaces are allowed. At least one unit must be present.

Examples:
    "1h30m"   -> 5400
    "45s"    -> 45
    "2h"     -> 7200
    "1h0m5s" -> 3605

Invalid strings raise ``ValueError``.
"""

import re

_PATTERN = re.compile(r"^(?:(?P<hours>\d+)h)?(?:(?P<minutes>\d+)m)?(?:(?P<seconds>\d+)s)?$")


def parse_duration(text: str) -> int:
    """Parse *text* and return the total number of seconds.

    Parameters
    ----------
    text: str
        The duration string to parse.

    Returns
    -------
    int
        Total seconds represented by *text*.

    Raises
    ------
    ValueError
        If *text* does not conform to the required format.
    """
    if not isinstance(text, str) or text == "":
        raise ValueError("duration string must be non‑empty")

    match = _PATTERN.fullmatch(text)
    if not match:
        raise ValueError(f"invalid duration format: {text!r}")

    # Ensure at least one component is present
    if not any(match.group(name) is not None for name in ("hours", "minutes", "seconds")):
        raise ValueError("duration string must contain at least one component")

    hours = int(match.group("hours")) if match.group("hours") is not None else 0
    minutes = int(match.group("minutes")) if match.group("minutes") is not None else 0
    seconds = int(match.group("seconds")) if match.group("seconds") is not None else 0

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
