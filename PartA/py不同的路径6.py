

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m][n]


if __name__ == "__main__":
	s = Solution()
	list2= [[0,0,0],
	        [0,1,0],
	        [0,0,0]]

	print(s.uniquePathsWithObstacles(list2))

