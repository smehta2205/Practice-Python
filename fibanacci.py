"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fibonacci(n):
    count = 2
    first = 1
    second = 1
    result_list = [1, 1]
    while count < n:
        third = first + second
        result_list.append(third)
        first = second
        second = third
        count += 1

    return result_list


if __name__ == "__main__":
    n = int(input("How many Fibonacci numbers you want to generate?"))
    result = fibonacci(n)
    print(result)
