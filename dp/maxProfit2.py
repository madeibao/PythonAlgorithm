
# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/31/星期六 16:12
# @File: maxProfit2.py

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2, 6, 4]
    ans = sol.maxProfit(nums)

