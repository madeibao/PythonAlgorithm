class Solution(object):
    def candy(self, ratings) ->int:
        """
        :type ratings: List[int]
        :rtype: int
        """
        if ratings == None:
            return 0
        lenth = len(ratings)
        dp = [1 for i in range(lenth)]
        sum = 0
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and dp[i] <= dp[i+1]:
                dp[i]=dp[i+1]+1
                
        for i in range(lenth):
            sum += dp[i]
        return sum


解法二：
class Solution():
    def candy(self, data) -> int:

        dp1 = [1 for i in range(len(data))]
        dp2 = [1 for i in range(len(data))]

        for i in range(1, len(data)):
            if data[i] > data[i-1]:
                dp1[i] = dp1[i-1] + 1

        for i in range(len(data)-2, -1, -1):
            if data[i] > data[i+1]:
                dp2[i] = dp2[i+1]+1

        sum = 0
        for i in range(len(data)):
            sum += max(dp1[i], dp2[i])

        return sum

cc = Solution()
print(cc.candy([1, 0, 2]))