def calculate_Global_commercial(amount):
    return int(amount) * 2.5


def calculate_Global_produced(amount_produced, amount_defective):
    return (amount_produced * 10) -  (amount_defective * 1.3)
