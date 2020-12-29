

while True:
	try:
				
		# 需要加密字符串
		str2 = input()
		# 需要解密字符串
		str3 = input()

		EncripT = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		EncripM = "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA1234567890"


		res2 = ""

		for i in str2:	
			temp = EncripT.find(i)
			res2 += EncripM[temp]

		res3 = ""
		for j in str3:
			temp = EncripM.find(j)
			res3 += EncripT[temp]

		print(res2)
		print(res3)

	except:
		break

		
# 需要加密字符串
str2 = input()

# 需要解密字符串
str3 = input()


EncripT = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
EncripM = "bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA1234567890"


res2 = ""

for i in str2:	
	temp = EncripT.find(i)
	res2 += EncripM[temp]


res3 = ""

for j in str3:
	temp = EncripM.find(j)
	res3 += EncripT[temp]

print(res2)
print(res3)

