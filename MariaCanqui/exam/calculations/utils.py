import re

code_commercial = []
code_production = []

def validate_amount(amount):
    while True:
        if re.fullmatch("([[1][0-5]|[3-9])",amount): return int(amount)
        else: amount = input("invalid amount, try again: ")

def validate_department(dep):
    while True:
        if re.fullmatch("commercial|production",dep.lower()): return dep
        else: dep = input("invalid department, try again: ")

def define_code(dep):
    global code_commercial
    global code_production
    if re.fullmatch("commercial", dep.lower()):
        size = len(code_commercial)+1
        code_commercial.append("CE_"+ str(size))
        return "CE_"+ str(size)

    if re.fullmatch("production", dep.lower()):
        size = len(code_production)+1
        code_production.append("PE_"+ str(size))
        return "PE_"+ str(size)


def validate_int(num):
    while True:
        if num.isdigit(): return int(num)
        else: num = input("invalid amount, try again: ")

