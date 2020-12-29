

while True:
	try:
		n = list(map(int, input().strip().split(" ")))
		res = []
		for i in range(len(n)-1):
			res.append(n[i]**n[i+1])
		print(" ".join(res))

	except:
		break

