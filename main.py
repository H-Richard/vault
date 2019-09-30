import os
import Generator
import mysql.connector
import getpass
import json
import ASCII
import CRUD

mkeyprompt = "Please choose a non-empty masterkey:\n"
mkey2prompt = "Please re-enter your masterkey:\n"

action_prompt = """ACTIONS:
C - Create a password
R - Retrieve a password
E - Exit the Program
D - Delete an entry (USE WITH CAUTION!)
Q - Query data [Usage: Q username_email, Q website...]\n"""

def main():

    master = False

    ASCIIascii()

    with open('config.json') as json_file:
        data = json.load(json_file)
    print()

    db = mysql.connector.connect(
          host=data["host"],
          user=data["user"],
          passwd=data["passwd"]
        )


    mycursor = db.cursor(buffered=True);
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        if 'main' == x[0]:
            mycursor.execute("USE main")
            master = True;
            break;
    else:
        mycursor.execute("CREATE DATABASE main")
        mycursor.execute("USE main")
        mycursor.execute("CREATE TABLE passwords (website VARCHAR(255), \
        username_email VARCHAR(255), password VARCHAR(255), PRIMARY KEY(website, username_email))")

        mkey = mkeysetup()

        mycursor.execute("INSERT INTO passwords VALUES(%s, %s, %s)", ("SYSTEM", "MASTER", mkey))
        db.commit()
        master = True;


    key = getpass.getpass(prompt = "Please enter your masterkey:\n")

    mycursor.execute("SELECT password FROM passwords WHERE website = %s AND \
                               username_email = %s", ("SYSTEM", "MASTER"))
    myresult = mycursor.fetchone()

    while key != myresult[0]:
        key = getpass.getpass(prompt = "Your masterkey was wrong! Please re-enter your master key:\n")

    action = ''
    if master:
        while action == '':
            action = input(action_prompt)

            if action.lower() == 'e':
                master = False;
                break;

            if action.lower() == 'c':
                CRUD.creatpswd(mycursor)
                action = ''

            if action.lower() == 'r':
                CRUD.retreivepswd(mycursor)
                action = ''

            if action.lower() == 'd':
                CRUD.deletepswd(mycursor)
                action = ''
        db.commit()               
        
    db.commit()
    mycursor.close()

if __name__ == "__main__":
    main()