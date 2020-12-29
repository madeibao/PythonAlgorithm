

#去除字符串中的所有的重复的元素



while True:
	try:
		str2 = input()
		list3 = []
		list2 = list(str2)
		for i in list2:
			if i not in list3:
				list3.append(i)
		print("".join(list3))
	except:
		break