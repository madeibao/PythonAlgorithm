

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(nums,i,j):
        	while i<j:
        		temp = nums[i]
        		nums[i] = nums[j]
        		nums[j] = temp
 				i+=1
 				j-=1
 			return nums

 		k = k%len(nums)

 		rotate(nums,0,len(nums)-k-1)
 		rotate(nums,len(nums)-k-1,len(nums)-1)
 		rotate(nums,0,len(nums)-1)

 		return nums


if __name__ == "__main__":
	s =Solution()
	print(s.rotate([1,2,3,4,5,6,7],3))

