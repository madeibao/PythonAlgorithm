
# recently viewed file: DFS/islandPerimeter.py
# this is a dfs problem, solve the perimeter of the island, the 
# island is represented by 1 and water is represented by 0,
# the perimeter is the number of edges that are adjacent to water or the edge of the grid.

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
                return 1
            if grid[i][j]==-1:
                return 0
            grid[i][j]=-1
            return dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0

if __name__ == "__main__":
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    solution = Solution()
    print(solution.islandPerimeter(grid))

