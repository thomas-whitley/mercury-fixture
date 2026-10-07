'''Utility for parsing duration strings like '1h30m' into seconds.'''

import re

# Matches optional hours, optional minutes, optional seconds in order.
# Each component is a sequence of digits followed by its unit letter.
_DURATION_RE = re.compile(r'^(?:(?P<h>\d+)h)?(?:(?P<m>\d+)m)?(?:(?P<s>\d+)s)?$')


def parse_duration(text: str) -> int:
    """Parse a duration string and return the total number of seconds.

    The string may contain an integer followed by ``h``, ``m`` or ``s`` in that order,
    each at most once and without spaces. At least one component must be present.

    Examples
    --------
    >>> parse_duration("1h30m")
    5400
    >>> parse_duration("45s")
    45
    """
    if not isinstance(text, str):
        raise ValueError("duration must be a string")

    match = _DURATION_RE.fullmatch(text)
    if not match:
        raise ValueError(f"invalid duration: {text!r}")

    groups = match.groupdict()
    # Ensure at least one component was supplied (e.g., empty string should fail)
    if not any(v is not None for v in groups.values()):
        raise ValueError(f"invalid duration: {text!r}")

    hours = int(groups["h"]) if groups["h"] is not None else 0
    minutes = int(groups["m"]) if groups["m"] is not None else 0
    seconds = int(groups["s"]) if groups["s"] is not None else 0
    return hours * 3600 + minutes * 60 + seconds
