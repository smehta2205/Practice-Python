"""
Created on Wed Oct 10 17:05:03 2018

@author: Gabriel
"""

l = [11,10,8,9,9,9,9,8,8,11]

def compare(list):
    newList = []
    for x in list:
        if x not in newList:
            newList.append(x)    
    return newList

x = compare(l)
print(x)