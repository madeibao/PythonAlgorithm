


for num in range(10,20):
	for i in range(2,num):
		if num%i==0:
			j=num/i
			print("%d 等于 %d * %d " %(num,i,j))
			continue
		else:
			print(num,"是个质数")
			continue