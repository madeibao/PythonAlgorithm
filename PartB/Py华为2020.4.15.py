
# 字典的多条件的排序

# list2 = input().strip().split(",")

def fun(str2):
	list3 = list(str2)

	if ord(list3[0])<65 or ord(list3[0])>90:
		return False

	for i in (1,len(list3)-1):
		if ord(list3[i])<97 or ord(list3[i])>122:
			return False
	return True

def test(list3):
	list2 = list3.strip().split(",")

	for i in list2:
		if fun(i)==True:
			continue
		else:
			return "error.0001"

	dict2 = {}

	for i in list2:
	    dict2[i] = dict2.get(i, 0) + 1

	temp = 0
	for value in dict2.values():
		temp += value

	if temp<0 or temp>100:
		return "error.0001"

	l = sorted(dict2.items(), key=lambda s:(-s[1], s[0]))
	return l[0][0]


list2 = input()
print(test(list2))
