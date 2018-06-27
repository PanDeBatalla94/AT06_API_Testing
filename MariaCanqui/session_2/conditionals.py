# Determine odd even numbers
def determine_odd_even(number):
    if number % 2 == 0: print("even")
    else: print("odd")


# Determine prime number
def determine_prime_number(list):
    for number in range(list[0], list[1]+1):
        count = 0
        for i in range(2, number - 1):
            if number % i == 0:
                count += 1
        if count > 0: print(str(number) + " Not prime")
        else: print(str(number) + " Prime")


print("determine if [1, 4] is prime")
determine_prime_number([1, 4])
print("determine if [4, 6] is is prime")
determine_prime_number([4, 6])
print("determine if [7, 9] is is prime")
determine_prime_number([7, 9])

print("determine if 2 is odd or even:")
determine_odd_even(2)
print("determine if 3 is odd or even:")
determine_odd_even(3)
print("determine if 1 is odd or even:")
determine_odd_even(5)
