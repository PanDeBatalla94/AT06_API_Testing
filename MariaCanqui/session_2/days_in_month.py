import calendar
list = calendar.mdays




def days_in_month(month_name):
    return {
        'January': calendar.monthrange(2018, 1)[1],
        'February': calendar.monthrange(2018, 2)[1],
        'March': calendar.monthrange(2018, 3)[1],
        'April': calendar.monthrange(2018, 4)[1],
        'May': calendar.monthrange(2018, 5)[1],
        'June': calendar.monthrange(2018, 6)[1],
        'July': calendar.monthrange(2018, 7)[1],
        'August': calendar.monthrange(2018, 8)[1],
        'September': calendar.monthrange(2018, 9)[1],
        'October': calendar.monthrange(2018, 10)[1],
        'November': calendar.monthrange(2018, 11)[1],
        'December': calendar.monthrange(2018, 12)[1]

    }.get(month_name, 0)

print("Days in January", str(days_in_month("January")))

print("Days in February", str(days_in_month("February")))