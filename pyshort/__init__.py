import random
import string

lower_str = string.ascii_lowercase
upper_str = string.ascii_uppercase
digits = string.digits
code_gen = lower_str + upper_str + digits


def short(code=code_gen, size=4, extra_string=None):
    if extra_string is not None:
        code += extra_string
    return ''.join(random.choice(code) for _ in range(size))
