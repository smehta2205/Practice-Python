def fibonacci(count):
    fib = [0, 1]
    for x in range(count-2):
        fib.append(fib[::-1][0] + fib[::-1][1])
    return fib

count = input("How many numbers generate in fibonacci")
print(fibonacci(count))

