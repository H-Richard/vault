import Generator

login = open('login.txt')

db = {}

master = ''

for line in login:
    if 'master' in line:
        temp = line.split(':')
        master = temp[1]

access = False

login = open('login.txt', 'a')

if master == '':
    while True:
        master = input('Please select a master key')
        line = 'master:' + master
        login.write(line)
        break
if master != '':
    key = input('Please enter your master key')
    if key == master:
        access = True
        print('Access granted')

if access:
    backup = open('backup.txt')
    for line in backup:
        temp = line.split(';')
        db[temp[0]] = temp[1]

    action = ''
    if action == '':
        action = input('Enter C at any time to create a new password or R to retrieve')

    if action == 'C' or action == 'c':
        backup_file = open('backup.txt', 'a')
        while True:
            username = input('Username')
            length = input('Length')
            usage = input('Usage')
            Generator.creation(username, usage, int(length), db)
            Generator.backup(username, db, backup_file)
            action = input('Enter C at any time to create a new password or R to retrieve')
            break





backup.close
login.close()