Input = input("Enter a long string ")
words = Input.split(" ")
inputWords = words[-1::-1]
output = ' '.join(inputWords)
print(output)

