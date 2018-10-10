def printDivisors(n) : 
    i = 1
    while i <= n : 
        if (n % i==0) : 
            print(i) 
        i = i + 1

num = int(input('>'))
print(f"The divisors of {num} are: ")
printDivisors(num) 
  

