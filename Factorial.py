N = int(input())

result = 1

for i in range(N,1,-1):
    result *= i
    print(i)
print(result)