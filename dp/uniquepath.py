

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 or n == 1:
            return 1
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


# 第二种解法，空间复杂度更低

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


# 第三种解法，空间复杂度更低
# 用数学的组合公式求解
# 由于是从左上角走到右下角，总共需要向右走 m - 1 步，向下走 n - 1 步
# 所以总共的路径数就是 C(m + n - 2, m - 1)
# 总体上，用C(m + n - 2, m - 1) 和 math.comb(m + n - 2, n - 1) 是一样的

# 组合公式：C(n, k) = n! / (k!(n-k)!)
# C(n, k) = C(n, n-k) = n! / (k!(n-k)!), 组合公式是对称的，所以只需要计算其中一个即可

import math
class Solution3(object):
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)


if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()

    print(solution.uniquePaths(m, n))
    # Output: 28