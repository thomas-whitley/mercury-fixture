import re


def parse_duration(text: str) -> int:
    if not text:
        raise ValueError("Empty duration")

    pattern = r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$"
    match = re.match(pattern, text)

    if not match or match.group(0) == "":
        raise ValueError(f"Invalid duration format: {text}")

    hours, minutes, seconds = match.groups()

    # If the match is empty (e.g. just invalid characters that didn't match pattern, though ^...$ handles that)
    # Also ensure there's at least one component present
    if hours is None and minutes is None and seconds is None:
        raise ValueError(f"Invalid duration format: {text}")

    total_seconds = 0
    if hours is not None:
        total_seconds += int(hours) * 3600
    if minutes is not None:
        total_seconds += int(minutes) * 60
    if seconds is not None:
        total_seconds += int(seconds)

    return total_seconds
