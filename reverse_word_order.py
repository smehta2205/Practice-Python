"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""


def reverse_word_order(sentence):
    """
    here, we will take the whole sentence, split it with <space> as delimiter and the print the list in reverse order
    :param sentence:
    :return:
    """
    word_list = sentence.split()
    reversed_order = ' '.join(word_list[::-1])
    print(reversed_order)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    reverse_word_order(sentence)
