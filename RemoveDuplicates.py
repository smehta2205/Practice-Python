# Remove Duplicates


def remove_duplicates(original_item):
    """
    Takes a list.
    Creates a new list which is a copy of the original list with all duplicates removed.
    Returns the new list.
    """

    if isinstance(original_item, list):
        # The original  item is a list.
        
        try:
            # We use a try because this is the version for non multi dimentional
            # list like one given in example 1

            # We use a set because it's more fun :)
            # Actually a set can't have a duplicate so we basically try to add
            # an element into seen. It it's working, then the element is not already
            # present.
            #
            # Note: seen.add() has no effect if the element in already into the set :)
            #
            # Note: Ofently you will see something like
            #   return list(set(element))
            # It's correct but the difference with the following is that we keep the order
            # when the example in this note does not keep the order.
            # But both (the note example and the following code) only work with
            # unidimentional list :)
            seen = set()

            return [element for element in original_item if not (element in seen or seen.add(element))]
        except TypeError:
            # This is the part for multi-dimentional list :)

            # We initiate a result which will save our element.
            result = []

            for element in original_item:
                # We loop through our list of element.

                if element not in result:
                    # The element is not already into our result.

                    # So we append it to our result :)
                    result.append(element)

            # We finaly return our list without duplicate :)
            return result


if __name__ == '__main__':
    # Because we may want to import only the function we add the
    # following condition which only works if you call for example
    # `python RemoveDuplicates.py`.

    # Example
    original_list = [1, "ABC", [1, 2, 3], 1,
                     "CDE", ["ABC", 2, 3], 1, "ABC", [123]]
    new_list = remove_duplicates(original_list)

    # We test our result.
    #
    # Note: An `assert` test a condition and it is not correct, it returns the
    # message.
    assert new_list == [1, 'ABC', [1, 2, 3], 'CDE', ['ABC', 2, 3], [
        123]], "Something went wrong with the testing of multi dimensional list."

    # Example 2
    original_list = [5, 1, 4, 1, 6, 5, 8]
    new_list = remove_duplicates(original_list)

    assert new_list == [
        5, 1, 4, 6, 8], "Something went wrong with the order or the deletion of duplicates."

    # Example 3
    original_list = [100, "hello", "you", "hello",
                     578, "world", "git", "100", 100, "world", 578]
    new_list = remove_duplicates(original_list)

    assert new_list == [100, "hello", "you", 578, "world", "git",
                        "100"], "Something went wrong with the order or the deletion of duplicates."

    print('All tests passed, the function is correct!')
