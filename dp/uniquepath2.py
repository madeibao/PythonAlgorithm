

# 整理的场景是带有障碍物的网格，机器人从左上角走到右下角有多少种不同的路径。

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        
        return dp[-1][-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()

    print(solution.uniquePathsWithObstacles(obstacleGrid))
    # Output: 2