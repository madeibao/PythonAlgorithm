





class Solution(object):
	def permutation(self,nums):

		res = []
		def helper(start):
			if start==len(nums):
				res.append(nums.copy())
			for i in range(start, len(nums)):
				nums[start],nums[i]= nums[i],nums[start]
				helper(start+1)
				nums[start],nums[i]= nums[i],nums[start]
		helper(0)

		return res

if __name__=='__main__':
	s = Solution()
	list2 = [1,2,3]
	print(s.permutation(list2))

