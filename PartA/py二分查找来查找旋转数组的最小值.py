

# 一个旋转数组，求旋转数组中的最小的值。

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]


if __name__ == "__main__":
	s = Solution()
	list2 = [3,4,5,1,2]
	print(s.findMin(list2))

