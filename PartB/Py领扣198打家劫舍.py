

# 输入: [2, 7, 9, 3, 1]
# 输出: 12
# 解释: 偷窃
# 1
# 号房屋(金额=2), 偷窃
# 3
# 号房屋(金额=9)，接着偷窃
# 5
# 号房屋(金额=1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        last = 0
        now = 0
        for i in nums:
            # 这是一个动态规划问题
            last, now = now, max(last + i, now)   # 两个值进行交换
        return now
#-----------------------------------------------------------------------------


# 动态规划的思路来进行。
from typing import List

class Solution():
    def rob(self,nums:List[int])->int:
        pre, now = 0, 0

        for i in range(len(nums)):
            temp = max(pre+nums[i],now)
            pre = now
            now = temp
        return now  


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))


#----------------------------------------------------------------------------

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return dp[len(nums) - 1]


if __name__ == '__main__':

    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))

































