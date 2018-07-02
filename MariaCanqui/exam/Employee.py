from Person import Person
class Employee(Person):
    def __init__(self, name, employeeId, department, globalSalary):
        super().__init__(name)
        self.employeeId = employeeId
        self.department = department
        self.globalSalary = globalSalary
        self.totalDiscount = self.calculate_discount()

    def calculate_discount(self):
        return (self.globalSalary *12.5)/100

    def get_netSalary(self):
        return self.globalSalary - self.totalDiscount

    def get_department(self):
        return self.department

    def get_globalSalary(self):
        return self.globalSalary

    def get_totalDiscount(self):
        return self.totalDiscount

    def get_employeeId(self):
        return self.employeeId



