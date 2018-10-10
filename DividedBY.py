number = int(input("Write a number "))
div = []
for i in range(1,number+1):
    
    if ((number % i) == 0):
        div.append(i)