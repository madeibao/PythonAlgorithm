
from typing import List

class Solution:
    def reverseLeftWords(self, nums: List[int], n: int) -> List[int]:

        def rotate(nums,i,j):
            while i<j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
                j-=1

        if len(nums)==0:
            return []

        if len(nums)==1:
            return nums
        
        len2 = len(nums)

        n = n%len2

        rotate(nums,0, n-1)
        rotate(nums,n,len2-1)
        rotate(nums,0, len2-1)

        return nums


if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,4,5,]
    n =2 #
    print(s.reverseLeftWords(nums, n))

    