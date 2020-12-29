# 有障碍物的独一无二的路径的内容
# 有障碍物的独一无二的路径的内容

class Solution(object):
    def uniquePaths(self, nums):

        m = len(nums)
        n = len(nums[0])

        dp = [[0] * n for _ in range(m)]

        for j in range(n):
            if nums[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(m):
            if nums[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if nums[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]



if __name__ == '__main__':
    s = Solution()
    nums = [[0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
    print(s.uniquePaths(nums))

