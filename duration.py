import re


def parse_duration(text: str) -> int:
    if not text:
        raise ValueError("Empty duration")

    # Pattern to match optional hours, minutes, and seconds in exact order: h then m then s.
    # Each can appear at most once, and the components must be contiguous.
    pattern = r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$"
    match = re.match(pattern, text)

    if not match or match.group(0) == "":
        raise ValueError(f"Invalid duration format: {text}")

    h_str, m_str, s_str = match.groups()

    # Ensure we didn't just match an empty string (though empty text is checked above)
    if h_str is None and m_str is None and s_str is None:
        raise ValueError(f"Invalid duration format: {text}")

    hours = int(h_str) if h_str else 0
    minutes = int(m_str) if m_str else 0
    seconds = int(s_str) if s_str else 0

    return hours * 3600 + minutes * 60 + seconds
