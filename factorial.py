fact = 1
n = int(input("Enter value:"))

for i in range(1,n+1):
    fact = fact * i

print("Factorial of " + str(n) + " is " + str(fact))

