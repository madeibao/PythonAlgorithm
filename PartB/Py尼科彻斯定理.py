


while True:
	try:
		n = int(input())
		temp = n * n - n + 1
		res = []

		for i in range(n):
		    res.append(str(temp))
		    temp += 2
		print("+".join(res))
	except:
		break