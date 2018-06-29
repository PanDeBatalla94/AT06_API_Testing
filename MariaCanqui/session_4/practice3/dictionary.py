import re
def create_list(size):
    user = {}
    for i in range(size):
        id = re.search('(100|[1-9][0-9]|[1-9])', input("userId"))
        if id == 0: id = 0
        else: id = id.group()



        if id == 0: id = id.group()
        name = re.match("\s{8}", input("userName: ")).group()
        user[id] = name
    return user


#print(create_list(2))
#string = input("userId: ")
print(re.match("\b{7}", "12345678910111213 d7").group())


