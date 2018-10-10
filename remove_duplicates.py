#!/usr/bin/env python3
# removes duplicate entries from a list


def remove_duplicates(input_list):
    """
    Takes a list and returns a new list that contains all the elements of the
    first list minus all the duplicates.
    """
    return list(set(input_list))


if __name__ == '__main__':
    print("remove_duplicates([1, 2, 3, 3, 4])")
    print(remove_duplicates([1, 2, 3, 3, 4]))
