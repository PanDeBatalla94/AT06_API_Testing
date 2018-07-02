import re
#Add a method that is going to ask for a username :

def ask_username():
    username = verify_username(input("enter username(a-z1-9 ): "))
    return username

#Need to be write with lowercase letter (a-z), number (0-9), an underscore
def verify_username(name):
    while True:
        if re.fullmatch("([a-z0-9 ]*)", name): return name
        else: name = input("Not valid user name, try again: ")

#Add a method that is going to ask for a password
def ask_password():
    password = verify_password(input("enter password (a-z),(0-9),(A-Z){8,16} : "))
    return password

#Need to be write with lowercase letter (a-z), number (0-9),
# letter (A-Z) and the length have to be between 8 and 16 characters

def verify_password(password):
    while True:
        if re.fullmatch("([a-zA-Z-0-9]{8,16})", password): return password
        else: password = input("Not valid password, try again: ")

#Add a method that is going to ask for email
def ask_email():
    email = verify_email(input("enter a valid email: "))
    return email

def verify_email(email):
    while True:
        if re.fullmatch("(\w+\@\w+\.\w{3}\.\w{2}|\w+\@\w+\.\w{3})", email): return email
        else: email = input("Not valid password, try again: ")


print(ask_username())
print(ask_password())
print(ask_email())
