

from typing import List, Tuple

'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:

        # 代表的是行
        m = len(grid)

        # 代表的是列。
        n = len(grid[0])

        # 这里多添加了一行和一列，为了简便运算。
        dp =[[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

'''

#============================================================================
# 算法2

class Solution():
    def maxValue(self,grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # dp = [[0]*n for i in range(m)]
        # 首先初始化第一行。

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        # 接着是初始化第一列的值。
        for j in range(1,m):
            grid[j][0] += grid[j-1][0]
        
        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]


if __name__ == "__main__":
    s = Solution()  
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1],            
    ]
    print(s.maxValue(grid))

