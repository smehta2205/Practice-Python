def simplePrimaryTest(value):
    if value == 2:
       return true
    if value % 2 == 0:
        return False
    
    i = 3
    sqrtOfValue = math.sqrt(value)
    
    while i <= sqrtOfValue:
        if value % i == 0:
            return False
        i = i+2
        
    return True  
