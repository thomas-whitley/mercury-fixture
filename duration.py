def parse_duration(text):
    if not text:
        raise ValueError("Invalid input")
    total_seconds = 0
    parts = text.split(':')
    for part in parts:
        if part[-1] == 'h':
            total_seconds += int(part[:-1]) * 3600
        elif part[-1] == 'm':
            total_seconds += int(part[:-1]) * 60
        elif part[-1] == 's':
            total_seconds += int(part[:-1])
        else:
            raise ValueError("Invalid input")
    return total_seconds

