#function
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 
duplicate = [int(x) for x in input("Enter a list of numbers: ").split()]
print(Remove(duplicate))
