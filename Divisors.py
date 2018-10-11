import math


def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.extend([i, n / i])
    divs.extend([n])
    return sorted(list(map(int, divs)))


num = int(input('Enter the number'))

print('Divisors of', num, ' are', divisors(num))
