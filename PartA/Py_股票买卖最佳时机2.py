# 买卖股票的最佳时机。


class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = float("inf")    # 表示正无穷大
        maxProfit = 0
        if len(prices) == 0:
            return 0
        for num in prices:
            if num < minPrice:
                minPrice = num
            if num - minPrice > maxProfit:
                maxProfit = num - minPrice
        return maxProfit
            


cc = Solution()
print(cc.maxProfit([7, 1, 5, 3, 6, 4]))