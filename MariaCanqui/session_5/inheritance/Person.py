class Person:
    def __init__(self, name, lastName, age, ci):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.ci = ci

    def get_complete_name(self):
        return self.name+ " "+ self.lastName



