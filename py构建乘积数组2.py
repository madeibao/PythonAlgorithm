


class Solution(object):
	def multiply(self,nums):

		list2 = [1]*len(nums)
		list3 = [1]*len(nums)

		left = 1
		right = 1

		res = [1]*len(nums)
		for i in range(1, len(nums)):
			left *= nums[i-1]
			list2[i]*= left

		for i in range(len(nums)-2,-1,-1):
			right *= nums[i+1]
			list3[i] *= right

		for i in range(len(nums)):
			res[i] = list2[i] * list3[i]
		return res


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,3,4,5]
	print(s.multiply(list2))

