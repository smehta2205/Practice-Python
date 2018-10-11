import math
def primality(number):
    for x in range(2, int(math.sqrt(number))):
        if number%x == 0:
            return False
    return True

print(primality(100))
print(primality(7691))
