



#只保留字符串的第一次出现的字符。


str2 = input()
str3 = []
for i in str2:
	if i not in str3:
		str3.append(i)

print("".join(str3))







