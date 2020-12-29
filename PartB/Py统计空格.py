

# aadddccddc
# dca


# a-z:97-122,A-Z:65-90,0-9:48-57
while True:	
	try:
		str2 = input()
		list2 = list(str2)
		dict2 = {}
		for i in list2:
		    if ord(i)>=48 and ord(i)<=57 or ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90 or ord(i)==32:
		        dict2[i] = dict2.get(i, 0) + 1
		l = sorted(dict2.items(), key=lambda s:(-s[1], s[0]))
		res = ""
		for i in l:
		    res+=i[0]
		print(res)
	except:
		break

# 方案2的办法。

import string
while True:
	try:
		str2 = input()
		list2 = list(str2)
		dict2 = {}
		for i in list2:
			if i in string.ascii_letters or i.isdigit() or i.isspace():
				dict2[i] = dict2.get(i,0) + 1
		l = sorted(dict2.items(), key=lambda s:(-s[1], s[0]))
		res = ""
		for i in l:
			res+= i[0]
		print(res)
	except:
		break

