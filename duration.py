"""Utility for parsing duration strings into seconds.

The supported format is a concatenation of integer values followed by
unit letters in the order hours (h), minutes (m), seconds (s). Each unit may
appear at most once and may be omitted, but at least one unit must be present.
Examples:
    "1h30m"   -> 5400
    "45s"     -> 45
    "2h"      -> 7200
    "1h0m5s"  -> 3605

Any deviation from this format raises :class:`ValueError`.
"""

import re

_PATTERN = re.compile(r"^(?:(?P<h>\d+)h)?(?:(?P<m>\d+)m)?(?:(?P<s>\d+)s)?$")


def parse_duration(text: str) -> int:
    """Parse *text* into a number of seconds.

    Parameters
    ----------
    text: str
        The duration string to parse.

    Returns
    -------
    int
        Total seconds represented by the string.

    Raises
    ------
    ValueError
        If the string does not conform to the required format.
    """
    if not isinstance(text, str) or text == "":
        raise ValueError("duration string must be non‑empty string")

    match = _PATTERN.fullmatch(text)
    if not match:
        raise ValueError(f"Invalid duration format: {text!r}")

    # Ensure at least one unit is present
    if not any(match.group(name) is not None for name in ("h", "m", "s")):
        raise ValueError(f"Invalid duration format (no units): {text!r}")

    hours = int(match.group("h")) if match.group("h") is not None else 0
    minutes = int(match.group("m")) if match.group("m") is not None else 0
    seconds = int(match.group("s")) if match.group("s") is not None else 0

    return hours * 3600 + minutes * 60 + seconds
