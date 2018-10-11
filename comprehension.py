def comprehension(arr):
    return [x for x in arr if x%2==0]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(comprehension(arr))
