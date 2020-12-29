
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
    
        m = len(grid)
        n = len(grid[0])

        # 初始化第一列的值。
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        # 初始化第一行的值。
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # 动态规划来实现。
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    nums = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    print(s.maxValue(nums))

