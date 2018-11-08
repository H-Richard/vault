import Generator

db = {}

pws = {}

access = False

welcome = input('Do you have an account? -Y/N')
if welcome == 'N' or welcome == 'n':
    while True:
        username = input('Please enter a username')
        password = input('Please enter a password')
        confirmation = input('Please confirm your password')
        if confirmation == password:
            db[username] = password
            welcome = 'Y'
            break
if welcome == 'Y' or welcome == 'y':
    while True:
        login_username = input('Please enter your username')
        login_password = input('Please enter your password')
        while login_username not in db:
            print('Username does not exist')
            login_username = input('Please enter your username')
        if db[login_username] == login_password:
            access = True
            print('Access granted')
            break
        else:
            print('Please try again')

if access:
    pws = Generator.storage
    action = input('Enter C at any time to create a new password')

    if action == 'C' or action == 'c':
        len = input('Length')
        usage = input('Usage')
        Generator.creation(int(len), usage)
