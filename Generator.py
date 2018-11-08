#!/usr/bin/env python
import random
import string
from typing import TextIO

backup_file = open('backup.txt', 'w')

storage = {}


def creation(usage:str,length:int) -> str:
    password = ''
    if usage in storage:
        print('Password usage already exists!')
        return
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    storage[usage] = password
    return password


def backup(key: str, storage:dict, file:TextIO) -> None:
    for keys in storage:
        if keys == key:
            file.write(key + ':' + storage[key])


def clear(file: TextIO) -> None:
    if input('Are you sure you want to clear the backup? -Y/N') == 'Y':
        open(file, 'w').close()


def retrieve(storage: dict, key) -> str:
    return storage[str(key)]
