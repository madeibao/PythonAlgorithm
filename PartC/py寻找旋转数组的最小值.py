


class Solution(object):
	def findMin(self,nums):
		left = 0
		right = len(nums) -1

		while left < right:
			mid = (left + right)>>1
			if nums[mid] >nums[right]:
				left = mid + 1
			else:
				right = mid 

		return nums[left]


if __name__ == "__main__":	
	s  = Solution()
	list2 = [4,5,1,2,3]
	print(s.findMin(list2))

