

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    	low = 0
    	high = len(nums) - 1

    	while low < high:
    		mid = (low + high)>>1
    		if mid ==len(nums)-1:
    			return mid 
    		if nums[mid]<nums[mid+1]:
    			low = mid +1
    		else:
    			high = mid 

    	return low


if  __name__ == "__main__":
	s = Solution()
	nums = [1,2,3,1]

	print(s.findPeakElement(nums))

