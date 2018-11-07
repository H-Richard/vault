import random
import string
from typing import TextIO

storage = {}


def creation(usage:str,length:int) -> str:
    password = ''
    if usage in storage:
        print('Password usage already exists!')
        return
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits)
    storage[usage] = password
    return password


backup_file = open('backup.txt', 'w')


def backup(key: str) -> None:
    for keys in storage:
        if keys == key:
            backup_file.write(key + ':' + storage[key] + '/n')
            backup_file.close()


def clear(file: TextIO) -> None:
    if input('Are you sure you want to clear the backup? -Y/N') == 'Y':
        open(file, 'w').close()
