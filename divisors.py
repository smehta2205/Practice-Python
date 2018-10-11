def divisors(number):
    div = []
    for i in range(1,number+1):
        if number%i == 0:
            div.append(i)
    return div

number = input("Write Number ")
print(divisors(number))    
