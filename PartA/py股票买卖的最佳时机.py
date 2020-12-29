


from typing import List, Tuple
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # inf = int(1e9)
        # minprice = inf


        minprice = float("inf")
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


if __name__ == "__main__":
    s = Solution()
    list2 = [7,1,5,3,6,4]
    print(s.maxProfit(list2))



#---------------------------------------------------------------------------------------------------------------------
# 买卖股票的最佳的时机2的方式。
# 多次的买卖一支股票来进行。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit

if __name__ == "__main__":
    s =Solution()
    list2 = [7,1,5,3,6,4]
    print(s.maxProfit(list2))




#------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class Solution():
    def maxprofit(self, nums):
        minprice= float("inf")
        maxprofit = 0

        for i in nums:
            maxprofit = max(i-minprice, maxprofit)
            minprice = min(i, minprice)

        return maxprofit

if __name__ == "__main__":
    s =Solution()

    list2 = [7,1,5,3,6,4]
    print(s.maxprofit(list2))

