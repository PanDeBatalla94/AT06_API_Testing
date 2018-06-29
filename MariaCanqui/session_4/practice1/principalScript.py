from practice1_module_age import age_to_minutes, age_to_hours, age_to_days
from practice1_module_messages import return_message

amount = int(input("Amount users: "))
user = {}
for i in range(amount):
    name = input("Name: ")
    age = int(input("Age: "))
    user[name] = age

for i in user:
    age = user[i]
    return_message(age)
    print(i, "information: ")
    print(age_to_minutes(age), "Minutes")
    print(age_to_hours(age), "Hours")
    print(age_to_days(age), "Days")