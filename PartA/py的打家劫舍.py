# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/6/9 9:21
# @File: Test.py


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], dp[i - 2] + nums[i]))
        # 因为是从0开始进行的。
        return dp[len(nums) - 1]


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3, 1]
    print(s.rob(list2))




