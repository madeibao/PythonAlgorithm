


# 矩阵的从左上角到右下角的最小额路径求和。


class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]

if __name__ == "__main__":
	s= Solution()
	list2 = [
	  [1,3,1],
	  [1,5,1],
	  [4,2,1]
	]
	print(s.minPathSum(list2))

