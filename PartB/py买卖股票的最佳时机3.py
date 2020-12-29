# @param prices int整型一维数组
# @return int整型

# 买卖股票的最佳的时机，表示为只能买卖一次。
# 动态规划。


class Solution:
    def maxProfit(self, prices):
        # write code here
        if not prices: return 0
        minp, maxp = float('inf'), float('-inf')
        for i in range(len(prices)):
            minp = min(minp, prices[i])
            maxp = max(maxp, prices[i] - minp)
        return maxp


if __name__ == '__main__':
    s = Solution()
    list2 = [1, 4, 2]
    list3 = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(list2))
    print(s.maxProfit(list3))


#--------=---------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

买卖股票的最佳时机，多次买卖
# @param prices int整型一维数组
# @return int整型
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit


if __name__ == "__main__":
    s = Solution()
    list2 = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(list2))



