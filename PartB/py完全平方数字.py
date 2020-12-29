



# 一个数字能够用最少的完全平方数字来表示出来。
# 求出最少的个数。


class Solution:
    def numSquares(self, n: int) -> int:
    	dp = [i for i in range(n+1)]
    	for i in range(1, n+1):
    		j = 1
    		while i-j*j >= 0:
    			dp[i] = min(dp[i], dp[i-j*j]+1)
    			j += 1
    	return dp[n]


if __name__ == "__main__":
	s =Solution()
	n =14
	print(s.numSquares(n))

