

class Solution:
    def minMoney(self , arr , aim ):
        dp = [float('inf')] * (aim + 1)
        dp[0] = 0

        for coin in arr:
            for x in range(coin, aim + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[aim] if dp[aim] != float('inf') else -1


if __name__ == '__main__':
	s = Solution()
	list2= [1, 2, 5]
	nums = 11
	print(s.minMoney(list2, nums))

	