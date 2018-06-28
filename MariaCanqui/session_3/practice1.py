dictionary = {}

def create_dictionary():
    global dictionary
    size = int(input("Dictionary length: "))
    for i in range(size):
        key = input("key: ")
        value = input("value: ")
        dictionary[key] = value
    return dictionary

def print_dictionary_keys():
    global dictionary
    print(dictionary.keys())

def print_dictionary_values():
    global dictionary
    print(dictionary.values())

def print_dictionary():
    global dictionary
    print(dictionary)

def search_key(key):
    global dictionary
    if key in dictionary: print("exists in", dictionary)
    else: print("not exists in", dictionary)

def search_value(value):
    global dictionary
    values = dictionary.values()
    if value in values: print("exists in", dictionary)
    else: print("not exists in", dictionary)


print(create_dictionary())
print_dictionary_keys()
print_dictionary_values()
print_dictionary()
search_key(input("Key to search: "))
search_value(input("Value to search: "))