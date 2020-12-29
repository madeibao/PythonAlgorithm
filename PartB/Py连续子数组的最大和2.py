

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] > 0 and nums[i - 1]
        return max(nums)

if __name__ == "__main__":
	s = Solution()
	list2 = [-2,1,-3,4,-1,2,1,-5,4]
	print(s.maxSubArray(list2))

	