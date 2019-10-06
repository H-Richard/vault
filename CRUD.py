import Generator
import mysql.connector
import getpass
import pyperclip

mkeyprompt = "Please choose a non-empty masterkey:\n"
mkey2prompt = "Please re-enter your masterkey:\n"

def mkeysetup() -> str:

    mkey = getpass.getpass(prompt = mkeyprompt)
    while not mkey:
        print("Your masterkey was empty!")
        mkey = getpass.getpass(prompt = mkeyprompt)

    mkey2 = getpass.getpass(prompt = mkey2prompt)
    while mkey2 != mkey:
        print("Your masterkeys did not match!")
        mkey2 = getpass.getpass(prompt = mkey2prompt)
    print("Setup complete, enter you masterkey 1 more time to begin!")
    return mkey

def creatpswd(mycursor):
    username = input('Please enter your username/email:\n')
    usage = input('Please enter the website/usage:\n')
    mycursor.execute("SELECT * FROM passwords WHERE username_email = %s AND website = %s", (username, usage))
    count = mycursor.rowcount
    if count == 0:
        length = int(input("Length of password:\n"))
        password = Generator.gen(length)
        pyperclip.copy(password)
        print("Password has been copied to the clipboard!~\n")
        mycursor.execute("INSERT INTO passwords (website, username_email, password) VALUES (%s, %s, %s)", (usage, username, password))
    else:
        print("username+usage already in database")

def retreivepswd(mycursor):
    usage = input('What is the usage/website?\n')
    username = input('What is the username/email?\n')
    mycursor.execute("SELECT * FROM passwords WHERE username_email = %s AND website = %s", (username, usage))
    count = mycursor.rowcount
    if count == 1:
        mycursor.execute("SELECT password FROM passwords WHERE website = %s AND \
                             username_email = %s", (usage, username))
        password = mycursor.fetchone()
        password = password[0]
        print('Your password: ' + password + " has been copied to the clipboard!~\n")
        pyperclip.copy(password)
    else:
        print('There is no such website/username combination in the database\n')

def deletepswd(mycursor):
    usage = input('What is the usage/website password would you like to delete?\n')
    username = input('What is the username/email?\n')
    mycursor.execute("SELECT * FROM passwords WHERE username_email = %s AND website = %s", (username, usage))
    count = mycursor.rowcount
    if count == 1:
        answer = input('Are you sure you want to delete this? Y/N\n')
        if answer.lower()!='y' and answer.lower()!='n':
            answer = input('Please enter Y or N\n')
        if answer.lower()=='y':
            mycursor.execute("DELETE FROM passwords WHERE website=%s AND username_email=%s", (usage, username))
    else:
        print('There is no such website/username combination in the database\n')
