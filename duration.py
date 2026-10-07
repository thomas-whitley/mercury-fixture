import re
def parse_duration(text):
    match = re.fullmatch(r'(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?', text)
    if not match or not text:
        raise ValueError("Invalid input")
    hours, minutes, seconds = match.groups()
    total_seconds = (int(hours or 0) * 3600) + (int(minutes or 0) * 60) + (int(seconds or 0))
    return total_seconds