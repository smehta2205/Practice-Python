import random
def main():
    array = [random.randint(1, 50) for _ in range(0, 10)]
    print("Unsorted")
    print(" ".join(str(x) for x in array))
    quicksort(array, 0, len(array) - 1)
    print("Sorted:")
    print(" ".join(str(x) for x in array))

def quicksort(array, p, r):
    if(p < r):
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)

def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if(array[j] <= x):
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1],array[r] = array[r],array[i + 1]
    return i + 1

main()

