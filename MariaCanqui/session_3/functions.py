#function 1
def fill_array():
    number = int(input("Number of elements: "))
    array = []
    for i in range(number):
        newElement = input("Element:")
        array.append(newElement)
    return array


print(fill_array())

#function 2
def fill_array(number):
    array = []
    for i in range(number):
        newElement = input("Element:")
        array.append(newElement)
    return array

print(fill_array(5))


