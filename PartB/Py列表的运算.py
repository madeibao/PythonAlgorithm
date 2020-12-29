

list2 = [1,2,3,4,5,6,7,8,9]

res= []

for i in range((len(list2))):
	temp = list2[:i]+(list2[i+1:])
	
print(res)

