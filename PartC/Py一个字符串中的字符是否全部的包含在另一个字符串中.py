
# BBDDCFFEL
# LCEFB
# true


if __name__ == '__main__':


	str2 = input()
	str3 = input()

	list2 = list(str2)
	list3 = list(str3)

	maxL, minL = [],[]

	if len(list2)>len(list3):
		maxL = list2
		minL = list3

	else:
		maxL = list3 
		minL = list2

	count =0

	for i in range(len(minL)):
		for j in range(len(maxL)):
			if minL[i]==maxL[j]:
				count += 1
				break


	if count== len(minL):
		print("true")
	else:
		print("false")

