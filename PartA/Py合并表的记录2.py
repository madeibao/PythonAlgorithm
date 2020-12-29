

n = int(input())

res = {}
for i in range(n):
	a,b = map(int, input().strip().split(" "))
	if a not in res.keys():
		res[a] = b
	else:
		res[a] += b

for key,value in res.items(): 
	print(str(key)+" "+str(value))
	