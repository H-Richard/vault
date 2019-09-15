import random
import string

def gen(length: int) -> str:
    password = ""
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password

def check_password(password: str) -> bool:
    nletter = 0
    nint = 0
    nspecial = 0
    i = 0
    while (i<len(password)):
        if password[i].isalpha():
            nletter += 1
        elif password[i].isnumeric():
            nint += 1
        else:
            nspecial += 1
        i += 1
    if (nletter>0 and nint > 0 and nspecial > 0):
        return True
    return False

def generator(length: int) -> str:
    password = gen(length)
    while not check_password(password):
        password = gen(length)
    return password


def main():
    password = generator(8)
    print(password)

if __name__ == "__main__":
    main()
