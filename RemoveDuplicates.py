#Remove Duplicates

def remove_duplicates(original_item):
    """
    Takes a list.
    Creates a new list which is a copy of the original list with all duplicates removed.
    Returns the new list.
    """
    # Create a new empty list
    new_list = []
    
    # Check if the item passed is a list
    if isinstance(original_item, list):
    
        # add each item to the new list if it's not already there.
        for item in original_item:
            if not item in new_list:
                new_list.append(item)
        
        # Return the new list.
        return new_list
        
    # If the original item is not a list, return it unchanged.    
    else:
        return original_item

# Example        
original_list = [1, "ABC", [1,2,3], 1, "CDE", ["ABC",2,3], 1, "ABC", [123]]
new_list = remove_duplicates(original_list)
print(new_list)

# Prints [1, 'ABC', [1, 2, 3], 'CDE', ['ABC', 2, 3], [123]]