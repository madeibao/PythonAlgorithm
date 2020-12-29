

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        max_dist = 1 #记录当前可以达到的最大长度
        while i<max_dist:
            max_dist = max(max_dist,i+nums[i]+1)
            if max_dist>=len(nums):
                return True
            i += 1
        return False

if __name__ == "__main__": 
    s = Solution()
    list2 = [2,3,1,1,4]
    print(s.canJump(list2))


