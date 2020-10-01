try:
    n = int(input("Enter a number"))
except:
    print("Please provide a valid integer number")
    
if n%2==0:
    print("Even number.")
print("Odd number.")
