
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        """
        计算从左上角到右下角的最小路径和（原地动态规划）

        每次只能向右或向下移动一步，直接在原网格上原地累加，
        状态转移方程：grid[i][j] += min(grid[i-1][j], grid[i][j-1])。

        Args:
            grid: m x n 的非负整数二维网格，函数会原地修改其内容

        Returns:
            从左上角到右下角的最小路径和
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 起点无需累加
                if i == j == 0: continue
                # 第一行只能从左侧过来
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                # 第一列只能从上方过来
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                # 其余位置取上方与左侧的较小值
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        # 右下角累计结果即为最小路径和
        return grid[-1][-1]


if __name__ == "__main__":
    nums = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    print(Solution().minPathSum(nums))