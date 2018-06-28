import math
def square():
    key = int(input("insert key in 1 - 9 range, another key fot exit: "))
    dictionary = {}
    while int(key) >= 1 and int(key) <= 9:
        dictionary[key] = math.pow(int(key),2)
        key = input("insert key in 1 - 9 range, another key fot exit: ")
        if key.isdigit() == False: break
    return dictionary

def extract_prime_numbers(dictionary):
    prime = {}
    for i in dictionary:
        count = 0
        for j in range(2, int(i)-1):
            if int(i) % j == 0:
                count = 1
        if count == 0:
            prime[i] = dictionary[i]

    return prime


dic = square()
print(dic)
print(extract_prime_numbers(dic))



