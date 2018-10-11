def userInput():
	list1 = []
	counter = 1
	while (counter < 11):
		try:
			num = int(input("Enter the number %d "%(counter)))
		except:
			print("Invalid Input.")
		else:
			list1.append(num)
			counter += 1
	return list1

def bubbleSort():
	list1 = userInput()
	for i in range(len(list1)):
		maximum = list1[0]
		for j in range(len(list1)-i):
			if (maximum <= list1[j]):
				maximum = list1[j]
				continue
			elif (maximum > list1[j]):
				temp = list1[j]
				list1[j] = maximum
				list1[j-1] = temp
		print(list1)
		for k in range(len(list1)-1):
			if (list1[k] < list1[k+1]):
				flag = True
				continue
			elif(list1[k] > list1[k+1]):
				flag = False
				break
		if(flag):
			break
		else:
			continue
bubbleSort()


