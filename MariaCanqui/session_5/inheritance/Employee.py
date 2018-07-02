from Person import Person
class Employee(Person):
    def __init__(self, name, lastName, age, ci, employeeId, deparment):
        super().__init__(name, lastName, age, ci)
        self.employeeId = employeeId
        self.deparment = deparment

    def get_employeId(self):
        return self.employeeId

    def get_department(self):
        return self.deparment

