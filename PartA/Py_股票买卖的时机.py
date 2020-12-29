
# 给定股票的最佳时机内容。
class Solution():
    def maxProfit(self,prices):
        sum2 = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp >0 :sum2 += temp 
        return sum2


if __name__ == "__main__":
    s= Solution()
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(s.maxProfit(list2))




