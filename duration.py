'''Parse duration strings like '1h30m' into total seconds.'''

import re

_PATTERN = re.compile(r'^(?:(?P<h>\d+)h)?(?:(?P<m>\d+)m)?(?:(?P<s>\d+)s)?$')


def parse_duration(text: str) -> int:
    """Return the number of seconds represented by *text*.

    *text* must consist of an integer followed by ``h``, ``m`` or ``s``,
    in that order, each at most once and without spaces.  At least one
    component must be present.  Invalid strings raise :class:`ValueError`.
    """
    match = _PATTERN.fullmatch(text)
    if not match:
        raise ValueError(f"Invalid duration: {text!r}")
    if not any(match.group(k) is not None for k in ("h", "m", "s")):
        raise ValueError("Empty duration")
    hours = int(match.group("h")) if match.group("h") else 0
    minutes = int(match.group("m")) if match.group("m") else 0
    seconds = int(match.group("s")) if match.group("s") else 0
    return hours * 3600 + minutes * 60 + seconds
