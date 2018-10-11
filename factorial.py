def factorail(number):
    total = 1
    for x in range(1, number+1):
        total = total * x
    return total

print(factorail(10))
