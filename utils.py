import re

def is_valid_entry(entry, type):
    if type == "name":
        return bool(entry.strip())
    elif type == "phone":
        return bool(entry.strip() and re.match(r'^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$', entry))
    elif type == "email":
        return bool(entry.strip() and re.match(r'[^@]+@[^@]+\.[^@]+', entry))
    elif type == "favorite":
        return entry.lower() in ["s", "n"]
    return False