list=[23,2,3,4,5,6,7,8,45,4,3.35,6.35,6.32]


def insertSort(arr):
	for i in range(1,len(arr)):
		j=i-1
		key=arr[i]
		while j>=0:
			if arr[j]>key:
				arr[j+1]=arr[j]
				arr[j]=key
			j -= 1
	return arr
	
print(insertSort(list))



#---------------------------------------------


def insertsort(num2):
    length = len(num2)

    for i in range(1, length):
        temp = num2[i]
        j = i-1
        while j >= 0 and num2[j] > temp:
            num2[j+1] = num2[j]
            j -= 1
        num2[j+1] =temp

    return num2


list2 = [2, 1, 2, 3, 3, 4, 5, 6, 67, ]
print(insertsort(list2))



