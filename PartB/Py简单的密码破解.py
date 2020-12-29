


str2 = input()

str3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
str4 = "bcdefghijklmnopqrstuvwxyza222333444555666777788899990123456789"


res = ""
for i in range(len(str2)):
	if str2[i] in str3:
		temp = str3.find(str2[i])
		res += str4[temp]

print(res)
