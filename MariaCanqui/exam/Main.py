import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from Employee import Employee
from calculations.utils import validate_amount
from calculations.utils import define_code
from calculations.utils import validate_department
from calculations.utils import validate_int
from calculations.salary_operations import calculate_Global_commercial
from calculations.salary_operations import calculate_Global_produced

handler = logging.FileHandler('application.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Start application')

amount = validate_amount(input("employees amount (3-15): "))
logger.debug('employees amount: '+str(amount))

logger.info('creation of employees dictionary .. ')
employees = {}

for i in range(amount):
    name = input("Employee name: ")
    department = validate_department(input("Employee Department(commercial|production): "))
    code = define_code(department)

    salary = 0
    if department == "commercial":
        amount_sell = validate_int(input("amount of pieces sell(number): "))
        salary = calculate_Global_commercial(amount_sell)

    if department == "production":
        amount_produced = validate_int(input("amount of pieces produced(number): "))
        amount_defective = validate_int(input("amount of pieces defective(number): "))
        salary = calculate_Global_produced(amount_produced,amount_defective)

    logger.debug('employee information: ' + str(name)+" "+str(department)+" "+str(code)+ " "+str(salary) )
    logger.info('creating object ...')
    print("-------------------------------------------")

    employees[i] = Employee(name, code, department, salary)

print("Employee Id | Name | Department | Global Salary | Total Discount | Net Salary")
for j in employees:
    print(employees[j].get_employeeId(),"       |",employees[j].get_name(),"|",employees[j].get_department(), "|",employees[j].get_globalSalary(),"|",employees[j].get_totalDiscount(),"|", employees[j].get_netSalary())


