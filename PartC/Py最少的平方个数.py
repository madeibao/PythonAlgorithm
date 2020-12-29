class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))





# 由于12 可以由4+4+4  最少三个平方数来求得。