import string
import random

def gen_key(parts = 4, chars_per_part = 8):
    alphaDig = string.ascii_uppercase + string.digits

    licence = []

    for _ in range(parts):
        licence.append("".join(random.choice(alphaDig) for _ in range(chars_per_part)))

    return "-".join(licence)
