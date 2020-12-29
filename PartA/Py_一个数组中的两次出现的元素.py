


class Solution():
	def mm(self,data):
		returnlist = []
		for x in data:
			if (data[abs(x)-1]<0):
				returnlist.append(abs(x))
			else:
				data[abs(x)-1] *= -1
		return returnlist

cc = Solution()
print(cc.mm([1,2,2,4,4,5]))


# 得出的结论为：[2,4]







