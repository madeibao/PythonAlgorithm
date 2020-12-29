


# 不同的路径的内容。
# 从左上角的位置上到右下角的位置上。

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n] * m
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 2
    s = Solution()
    print(s.uniquePaths(m, n))
















