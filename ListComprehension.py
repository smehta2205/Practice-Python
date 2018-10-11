# Use list comprehension to create one line of Python code theat makes a list
# of even numbers from the below list.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = [(i) for i in a if i % 2 == 0]

print(new_list)

# Prints:
# [4, 16, 36, 64, 100]