import string

def number_letters(sentence):
    alphabet = {}
    for letter in sentence.lower():
        if (letter in string.ascii_lowercase):
            if letter in alphabet:
                alphabet[letter] = int(alphabet[letter]) + 1
            else:
                alphabet[letter] = 1
    return alphabet

sentence = "ThiS is String with Upper and lower case Letters”, would look this this "
alphabet = number_letters(sentence)
for value in sorted(alphabet):
    print(value, ":", alphabet[value])