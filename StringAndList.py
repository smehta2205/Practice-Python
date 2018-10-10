# Function to reverse words of string 

def reverseWords(input): 
	
	# split words of string separated by space 
	inputWords = input.split(" ") ;
	inputWords=inputWords[-1::-1] 

	# now join words with space 
	output = ' '.join(inputWords) 

	return output 

if __name__ == "__main__": 
    name = input("What's your name? ")
    print (reverseWords(name)) 
   
