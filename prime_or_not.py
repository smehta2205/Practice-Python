def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

n=int(input("Enter A Number:"))
if isPrime(n):
    print(n,"is Prime.")
else:
    print(n,"is not Prime.")
