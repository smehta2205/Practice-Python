_FAC_TABLE = [1, 1]
def factorial(n):
    if n < len(_FAC_TABLE):
        return _FAC_TABLE[n]

    last = len(_FAC_TABLE) - 1
    total = _FAC_TABLE[last]
    for i in range(last + 1, n + 1):
        total *= i
        _FAC_TABLE.append(total)

    return total

def rFactorial(n):
   if n <1:
       return 1
   else:
       return n * factorial( n - 1 )

def main():
    n = int(input())
    print(factorial(n))
    print(rFactorial(n))


if __name__ == "__main__":
    main()
