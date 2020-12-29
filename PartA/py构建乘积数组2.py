

from typing import List, Tuple, Optional

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1,1
        list2 = [1]*len(nums)
        list3 = [1]*len(nums)
        res = [1]*len(nums)

        for i in range(1, len(nums)):
            list2[i] = list2[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            list3[i] = list3[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i] = list2[i]*list3[i]
        return res 

if __name__ == "__main__":
    s = Solution()
    list2 = [1,2,3,4]
    print(s.productExceptSelf(list2))


