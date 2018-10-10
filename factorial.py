n=int(input("Enter number:"))
fact=1
if n==0:
    print(fact)
else:
    while(n>0):
        fact=fact*n
        n=n-1
    print("Factorial of the number is: ")
    print(fact)
