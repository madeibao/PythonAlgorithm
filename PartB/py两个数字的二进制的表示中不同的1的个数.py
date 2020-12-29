




n, m = map(int,input().split(" "))
temp = n^m
res = 0

while temp:
	temp = temp&(temp-1)
	res+=1

print(res)

