

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 and nums[0]==target:return 0
        low,high=0,len(nums)-1

        
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:high=mid-1
            else:low=mid+1
        return -1

        

if __name__ == "__main__":
	s = Solution()
	nums = [5,7,7,8,8,10]
	target = 8

	print(s.search(nums, target))


