

# 从左上角到右下角的不同的路径的内容。


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__": 
	s = Solution()
	m = 3
	n = 2 
	print(s.uniquePaths(m, n))
