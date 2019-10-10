a=int(input("Enter first no.     "))
b=int(input("Enter second no.     "))
print("Your Options;Select one:")
print("+ for sum")
print("- for sub")
print("* for mul")
print("/ for div")
n=input("Your choice             ")
print("Result is...    ")
if n == '+':
    print(a + b)
elif n == '-':
    print(a - b)
elif n == '*':
    print(a * b)
elif n == '/':
    print(a / b)
else:
    print("Enter valid choice")
