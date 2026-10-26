def parse_duration(text):
    """Parse a duration string like ``'1h30m5s'`` into total seconds.

    The string may contain an integer followed by ``h`` (hours), ``m`` (minutes)
    and ``s`` (seconds) **in that order**, each at most once and without
    spaces. At least one component must be present. Invalid strings raise
    ``ValueError``.
    """
    import re

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Optional hour, then optional minute, then optional second – in order.
    pattern = re.compile(r'^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$')
    match = pattern.fullmatch(text)
    if not match:
        raise ValueError(f"Invalid duration format: {text!r}")

    hours, minutes, seconds = match.groups()
    # Disallow empty string (all groups None)
    if not any([hours, minutes, seconds]):
        raise ValueError("Duration string cannot be empty")

    total = 0
    if hours:
        total += int(hours) * 3600
    if minutes:
        total += int(minutes) * 60
    if seconds:
        total += int(seconds)
    return total
