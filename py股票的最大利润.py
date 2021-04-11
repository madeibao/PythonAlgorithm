


# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py股票的最大利润.py
@Time    :   2020/12/31 10:42:03
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""

# 动态规划算法的

class Solution(object):
    def maxProfit(self,nums):

        if len(nums)==0:return 0
        maxProfit = float("-inf")
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = min(temp, nums[i])
            maxProfit = max(maxProfit, nums[i]-temp)
        return maxProfit


if __name__ == "__main__":
    s = Solution()
    nums = [7,1,5,3,6,4]
    print(s.maxProfit(nums))






