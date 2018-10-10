import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

input_number = int(input("Enter a number: "))
if(is_prime(input_number)):
		print("Prime")
else:
		print("Not Prime")