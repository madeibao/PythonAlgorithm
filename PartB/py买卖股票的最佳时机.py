
# 可以多次的抛售和买卖股票的内容。
# 多次的抛售。

# 注意的是多次的抛售。

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0: profit += tmp
        return profit


if __name__ == "__main__":
    s = Solution()
    list2 =[7,1,5,3,6,4]
    print(s.maxProfit(list2))


# 下面的暴力算法会超时。
class Solution(object):
    def maxProfit(self,prices):
        maxprofit = 0

        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j]-prices[i]>maxprofit:
                    maxprofit = prices[j]-prices[i]

        return maxprofit

if __name__ == "__main__":
    s = Solution()
    list2 =[7,1,5,3,6,4]
    print(s.maxProfit(list2))

