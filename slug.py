def slugify(text):
    import re
    return re.sub(r'[^A-Za-z0-9]+', '-', text.lower()).strip('-')