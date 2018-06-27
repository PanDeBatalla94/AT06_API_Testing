def replace(string, old, new):
    return new.join(string.split(old))

string = "Mississippi"
print(replace(string, "i", "I"))

string = "I love spom!"
print(replace(string, "om", "am"))

string = "Spam,spam, yum!"
print(replace(string, "o", "a"))
