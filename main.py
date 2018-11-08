import Generator

db = {}

pws = {}

login_file = open('login.txt', 'r+')

welcome = ''

# iterates through login file to see if there is an existing user.
for line in login_file:
    # yes to user:
    if not (line == ''):
        welcome = 'Y'
    temp = line.split(':')
    db[temp[0]] = temp[1]
login_file.close()

login_file = open('login.txt', 'a+')
backup_file = open('backup.txt', 'a+')

access = False

if welcome == '':
    while True:
        username = input('Please enter a username')
        password = input('Please enter a password')
        confirmation = input('Please confirm your password')
        if confirmation == password:
            db[username] = password
            Generator.backup(username, db, login_file)
            welcome = 'Y'
            backup_file.close()
            break
if welcome == 'Y' or welcome == 'y':
    while True:
        login_username = input('Please enter your username')
        while login_username not in db:
            print('Username does not exist')
            login_username = input('Please enter your username')
        login_password = input('Please enter your password')
        if db[login_username] == login_password:
            access = True
            print('Access granted')
            break
        else:
            print('Please try again')


if access:
    backup_file = open('backup.txt', 'r')
    for line in backup_file:
        temp = line.split(':')
        db[temp[0]] = temp[1]

    pws = Generator.storage

    action = ''

    if action == '':
        action = input('Enter C at any time to create a new password or R to retrieve')

        if action == 'C' or action == 'c':
            backup_file = open('backup.txt', 'a+')
            while True:
                len = input('Length')
                usage = input('Usage')
                Generator.creation(usage, int(len))
                Generator.backup(usage, pws, backup_file)
                action = input('Enter C at any time to create a new password or R to retrieve')
                break
        if action == 'R' or action == 'r':
            while True:
                Generator.retrieve(backup_file, input('Enter your key'))
                action = input('Enter C at any time to create a new password or R to retrieve')
                break


login_file.close()
backup_file.close()