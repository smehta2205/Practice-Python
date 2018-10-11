"""Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."""

if __name__ == """__main__""":
  #Solution:
  nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  comprehension = [num for num in nums if num % 2 == 0]
  
  # This is the same as:
  # result = []
  # for num in nums:
  #   if num % 2 == 0:
  #     result.append(num)

  
  
  
  
