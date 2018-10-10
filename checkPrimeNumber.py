# Check prime number

# Input number from user
num = int(input("Input Number: "))

#check it
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is Not prime number")
            print(i, " x ", num//i, "=", num)
            break
    else:
        print(num,"is Prime Number")
        
else:
    print(num, "is Not prime number")
