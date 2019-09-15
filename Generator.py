import random
import string


def gen(length: int) -> str:
    password = ''
    while len(password) < int(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password
