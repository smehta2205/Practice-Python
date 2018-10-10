#taking input for the array from user
a = [int(x) for x in input().strip().split()]
b = [x for x in a if x%2 == 0]
print(b)
