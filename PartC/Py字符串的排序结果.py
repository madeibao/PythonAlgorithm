
while True:
	try:
		str2 = input()
		res = [0] *len(str2)
		s2 = []

		for k,v in enumerate(str2):
			if v.isalpha():
				s2.append(v)
			else:
				res[k] = v

		s2.sort(key=lambda x:x.upper())

		for k,v in enumerate(res):
			if not v:
				res[k]=s2[0]
				s2.pop(0)

		print("".join(res))

	except:
		break


