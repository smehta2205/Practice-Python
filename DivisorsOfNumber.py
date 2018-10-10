
# A O(sqrt(n)) program that prints all divisors in sorted order 
import math  
  
# Method to print the divisors 
def printDivisors(n) : 
    list = []  
      
    # List to store half of the divisors 
    for i in range(1, int(math.sqrt(n) + 1)) :
        if (n % i == 0) : 
        
            # Check if divisors are equal 
            if (n / i == i) : 
                print (i, end=" ") 
            else : 
                # Otherwise print both 
                print (i, end=" ") 
                list.append(int(n / i)) 
                  
    # The list will be printed in reverse     
    for i in list[::-1] : 
        print (i, end=" ") 
          
# Driver method 
number = int(input("Enter a number: "))
print ("\nThe divisors of entered number are: ") 
printDivisors(number)
