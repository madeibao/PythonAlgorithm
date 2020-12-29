

# 字符串中，大写转成小写，小写不变，其他字符统计入内。

str2 = input()
list2 = list(str2)

list3 = []
for i in list2:
	if i.isalpha():
		if ord(i)>=65 and ord(i)<=90:
			list3.append(i.lower())
		elif ord(i)>=97 and ord(i)<=122:
			list3.append(i)
		else:
			continue

print("".join(list3))





