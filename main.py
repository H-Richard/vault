import os
import Generator
import mysql.connector

action_prompt = "[C - Create a password, R - Retrieve a password]\n"


def main():

    master = False


    db = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="main"
        )

    mycursor = db.cursor();
    mycursor.execute("DROP DATABASE main")
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        if 'main' in x:
            master = True;
            break;
    else:
        mycursor.execute("CREATE DATABASE main")
        mycursor.execute("USE main")
        mycursor.execute("CREATE TABLE passwords (website VARCHAR(255), \
        username_email VARCHAR(255), password VARCHAR(255), PRIMARY KEY(website, username_email))")
        mkeyprompt = "Please choose a non-empty masterkey:\n"
        action = input(mkeyprompt)
        while not action:
            print("Your masterkey was empty!\n")
            action = input(mkeyprompt)
        mycursor.execute("INSERT INTO passwords VALUES(%s, %s, %s)", ("SYSTEM", "MASTER", action))
        master = True;


    key = input("Please enter your masterkey")

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
