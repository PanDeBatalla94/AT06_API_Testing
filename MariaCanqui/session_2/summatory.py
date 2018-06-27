def sum_to(n):
    sum = 0
    for i in range(n + 1):
        if i < 35: sum += i
        else: break
    return sum

print(str(sum_to(10)))
print(str(sum_to(40)))