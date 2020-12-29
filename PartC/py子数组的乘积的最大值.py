



# # 暴力破解的方法，
# # 求子数组的乘积的最大值。
# # 子数组的乘积
# 题目描述
# 给定一个double类型的数组arr，其中的元素可正可负可0，返回子数组累乘的最大乘积。
# 例如arr=[-2.5，4，0，3，0.5，8，-1]，子数组[3，0.5，8]累乘可以获得最大的乘积12，所以返回12。



class Solution():
	def subArray(self,nums):
		if not nums:
			return 0

		if len(nums)==1:return nums[0]

		res, temp = 0, 1
		for i in range(len(nums)):
			for j in  range(i, len(nums)):
				temp *= nums[j]
				res = max(res, temp)
			temp =1
		return res 


if __name__ == "__main__":
	s = Solution()
	list2 = [-2.5,4, 0, 3, 0.5, 8,-1]
	print(s.solve(list2))

