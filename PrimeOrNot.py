def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return True
    return False


num = int(input('Enter the number'))

if isPrime(num):
    print(num, ' is not prime')
else:
    print(num, ' is prime')
