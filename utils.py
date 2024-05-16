from string import ascii_letters, digits
from random import choice

def random_string(length):
    return ''.join(
        choice(digits + ascii_letters) 
        for _ in range(length))

raw_link = 't.me/{}?start='