import os
import Generator
import mysql.connector

action_prompt = "[C - Create a password, R - Retrieve a password]\n"


def main():

    master = False

    db = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password"
        )

    mycursor = db.cursor();


    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        if 'main' in x:
            break;
    else:
        mycursor.execute("CREATE DATABASE main")
        mycursor.execute("CREATE TABLE ")

    action = ''

    if master:
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
