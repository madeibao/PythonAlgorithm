

n = int(input())
list2 = list(map(int,input().split(" ")))

def isSame(a,b):
	if a&b != 0:
		return True
	return False

res = []

for i in range(len(list2)):
	temp = list2[:i]+list2[i+1:]
	print(temp)
	for j in range(len(temp)):
		if isSame(list2[i],temp[j]):
			res.append("-1")
		else:
			res.append("1")

print(res)
res2 = res[n-2::n-1]
print(" ".join(res2))