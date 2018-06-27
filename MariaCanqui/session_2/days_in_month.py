def days_in_month(month_name):
    return {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31

    }.get(month_name, None)

print("Days in January", str(days_in_month("January")))

print("Days in February", str(days_in_month("February")))

print("Days in Abc", str(days_in_month("Abc")))