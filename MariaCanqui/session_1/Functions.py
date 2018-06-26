def perform_operation(operator, case1, case2):
    return {
        '+': int(case1) + int(case2),
        '-': int(case1) - int(case2),
        '*': int(case1) * int(case2),
        '/': int(case1) / int(case2),
        '%': int(case1) % int(case2),
        '**': int(case1) ** int(case2),
        '//': float(case1) // float(case2)
    }.get(operator, 0)

print("Suma " + str(perform_operation("+", "3", "4")))
print("Substraction " + str(perform_operation("-", "7", "4")))
print("Multiplication " + str(perform_operation("*", "3", "4")))
print("Division " + str(perform_operation("/", "10", "5")))
print("Modulus " + str(perform_operation("%", "8", "2")))
print("Exponent " + str(perform_operation("**", "2", "3")))
print("Floor division " + str(perform_operation("//", "9.0", "2.0")))