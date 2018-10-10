def bubbleSort(arrayList):
    for num in range(len(arrayList)-1,0,-1):
        for i in range(num):
            if arrayList[i]>arrayList[i+1]:
                temp = arrayList[i]
                arrayList[i] = arrayList[i+1]
                arrayList[i+1] = temp

arrayList = [56,23,21,1,342,5,7,11,8,123,9,23]
bubbleSort(arrayList)
print(arrayList)
