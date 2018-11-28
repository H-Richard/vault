import os
import Generator

action_prompt = ['C - Create a password, R - Retrieve a password']


def main():

    action = ''

    pws = {}
    usrs = {}

    b_txt = 'backup.txt'

    b_lines = open(b_txt).readlines()

    master = False

    if os.stat(b_txt).st_size == 0:
        master_key = input('Please enter a masterkey')
        master_confirm = input('Please enter your masterkey again')
        if master_key == master_confirm:
            writable = open(b_txt, 'w')
            writable.write(master_key)

    elif os.stat(b_txt).st_size != 0:
        if '\n' not in b_lines[0]:
            master_key = b_lines[0]
        elif '\n' in b_lines[0]:
            master_key = b_lines[0][:b_lines[0].find('\n')]

        while not master:
            prompt = input('Please enter your masterkey')
            if prompt == master_key:
                master = True
            else:
                print('Error!')

    if master:
        for i in range(1, len(b_lines)):
            temp = (b_lines[i].split('-'))
            usr_pws = temp[1].split(':')
            pws[temp[0].lower()] = usr_pws[1]
            usrs[temp[0].lower()] = usr_pws[0]

        while action == '':
            action = input(action_prompt)

            if action.lower() == 'c':
                username = input('Please enter a username')
                usage = input('Please enter a usage/website')
                if usage in pws or usage in usrs:
                    print('You already have a login for this website!')
                    break
                length = input('Please enter a length')
                password = Generator.gen(int(length))
                print('this is your password:')
                print(password)
                appendable = open(b_txt, 'a')
                append = '\n' + usage + '-' + username + ':' + password
                appendable.write(append)
                action = ''
            if action.lower() == 'r':
                usage = input('What is the usage/website?')
                username = 'username' + ':' + usrs[usage]
                password = 'password' + ':' + pws[usage]
                print(username)
                print(password)
                action = ''


if __name__ == "__main__":
    main()
