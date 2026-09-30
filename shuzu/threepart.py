
from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        # 至少需要4个元素
        if n < 4:
            return False
        
        i = 0
        # 第一步：爬坡
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        # 检查
        if i == 0 or i == n - 1:
            return False
        
        # 第二步：下坡
        p = i
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
        # 检查
        if i == p or i == n - 1:
            return False
            
        # 第三步：再次爬坡
        q = i
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
        # 检查
        return i == n - 1

if __name__=="__main__":
    nums = [1,3,5,4,2,6]
    print(Solution().isTrionic(nums))
