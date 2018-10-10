Input = input('Enter a string ')
Reverse = Input[::-1]
if(Input.lower() == Reverse.lower()):
    print('String is Palindrome')
else:
    print('String is not Palindrome')
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
