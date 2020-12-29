
# 买卖股票只能能进行一次。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice= float("inf")
        maxprofit = 0

        for i in prices:
            maxprofit = max(i-minprice, maxprofit)
            minprice = min(i, minprice)

        return maxprofit


if __name__ == "__main__":
	s = Solution()
	list2= [7,1,5,3,6,4]
	print(s.maxprofit(list2))


# =========================================================================
# 股票可以买卖多次
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#----------------------------------------------------------------------------------------


from typing import List

class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0: profit += tmp
        return profit

if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(s.maxProfit(list2))

