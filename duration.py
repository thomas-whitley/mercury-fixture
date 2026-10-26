import re


def parse_duration(text: str) -> int:
    """Parse a duration string and return total seconds.
    
    Format: [hours]h[minutes]m[seconds]s where each unit appears at most once
    and in order h, m, s. No spaces allowed.
    
    Examples:
        "1h30m" -> 5400
        "45s" -> 45
        "2h" -> 7200
        "1h0m5s" -> 3605
    
    Raises:
        ValueError: if the format is invalid
    """
    if not text:
        raise ValueError("empty string")
    
    # Pattern to match the duration format
    # Each component is optional but must appear in order h, m, s
    pattern = r'^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$'
    match = re.fullmatch(pattern, text)
    
    if not match:
        raise ValueError(f"invalid duration format: {text}")
    
    hours_str, minutes_str, seconds_str = match.groups()
    
    # Check that at least one component is present
    if hours_str is None and minutes_str is None and seconds_str is None:
        raise ValueError(f"invalid duration format: {text}")
    
    hours = int(hours_str) if hours_str is not None else 0
    minutes = int(minutes_str) if minutes_str is not None else 0
    seconds = int(seconds_str) if seconds_str is not None else 0
    
    return hours * 3600 + minutes * 60 + seconds
