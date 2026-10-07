import re


def parse_duration(text: str) -> int:
    if not text:
        raise ValueError("Empty duration")

    pattern = r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$"
    match = re.match(pattern, text)

    if not match or match.group(0) == "":
        raise ValueError(f"Invalid duration format: {text!r}")

    h_str, m_str, s_str = match.groups()

    # Ensure at least one component was present
    if h_str is None and m_str is None and s_str is None:
        raise ValueError(f"Invalid duration format: {text!r}")

    total_seconds = 0
    if h_str is not None:
        total_seconds += int(h_str) * 3600
    if m_str is not None:
        total_seconds += int(m_str) * 60
    if s_str is not None:
        total_seconds += int(s_str)

    return total_seconds
