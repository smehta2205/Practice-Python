nums = []


def fibonacci(amount: int):
    a, b = 0, 1
    while len(nums) < amount:
        nums.append(a)
        a, b = b, a + b

to_generate = int(input("Enter the amount of numbers in the Fibonacci Sequence to generate: "))
fibonacci(to_generate)

print(", ".join([str(num) for num in nums]))
