import re

user = {}
coincidences = []
names = []
#Function that will create a dictionary with a list of userID and userName,
# the userID should be only numbers between 1 to 100. Username should be only
# lowercase (nor more than 8 digits)
def create_list(size):
    global user
    for i in range(size):
        id = verify_userId()
        name = verify_userName()
        user[id] = name
    return user

def verify_userId():
    id = input("enter user id (1-100): ")
    while True:
        if re.fullmatch('(100|[1-9][0-9]|[1-9])', id):
            return id
        else:
            id = input("Not valid id, try again:")

def verify_userName():
    name = input("enter user name (a-z) size 8: ")
    while True:
        if re.fullmatch('[a-z0-9 ]{1,8}', name):
            return name
        else:
            name = input("Not valid user name, try again:")

#Function that is going to request to the user for a number (only 1 number)
#  and need to return the amount of users that have their user ID starting
#  with the number inserted (E.g. if user inserted 1, then could count all
#  users with 1, 10,11,12,13..19 or 100), return and array with the user_ID
#  that fulfilled this condition

def amount_users_with_id_number(num):
    global user
    global coincidences
    for i in user:
        if (num in i): coincidences.append(i)
    return coincidences


#Function that is going to request to the user for a character (only 1 char)
#  and need to return the amount of users that have their  userName starting
#  with the character inserted (E.g. if user inserted a, then could count all
#  users that start with a), return and array with the list of userName that
#  fulfilled this condition
def user_name_by_character(character):
    global user
    global names
    for i in user:
        if re.search("^"+character, user[i]):
            names.append(user[i])
    return names

#Function to display a message considering :
#UseID between 1-25 “User belong Group 1”
#UseID between 26-50 “User belong Group 2”
#UseID between 51-75 “User belong Group 3”
#UseID between 76-100 “User belong Group 4”
def select_group():
    global user
    for i in user:
        if re.fullmatch("(2[0-5]|[1[0-9]|[1-9])", i):
            print("id: ", i, "user", user[i], "User belong Group 1")
        elif re.fullmatch("(2[6-9]|[3-5][0-9])", i):
            print("id: ", i, "user", user[i], "User belong Group 2")
        elif re.fullmatch("5[1-9]|[6-7][0-9]|7[1-5]]", i):
            print("id: ", i, "user", user[i], "User belong Group 3")
        elif re.fullmatch("7[6-9]|[8-9][0-9]|100", i):
            print("id: ", i, "user", user[i], "User belong Group 4")


#1
print(create_list(int(input("List size: "))))
#2
print(amount_users_with_id_number(input("Search id that contains number: ")))
#3
print(user_name_by_character(input("Names started in:")))
#4
select_group()
