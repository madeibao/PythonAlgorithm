

# 在python中，一般情况是，'' 包含有""
#===================================

def muti(str2):
	list2 = list(str2[1:-1].split('","'))
	t= list2[0]
	list2[0] = ''.join(t[1:])

	end2 = list2[-1]
	list2[-1] = ''.join(end2)[:-1]


	res = 0
	for i in range(len(list2)-1):
		for j in range(i+1, len(list2)):
			if list(set(list2[i]) & set(list2[j]))== []:
				res =max(res, len(list2[i])*len(list2[j]))

	return res


if __name__ == "__main__":
	str2 =input()
	print(muti(str2))






