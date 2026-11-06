
# 腐烂的橘子，2表示腐烂的橘子，1表示新鲜的橘子，0表示空的单元格。
# 每一分钟，任何与腐烂的橘子相邻的新鲜橘子都会腐烂。

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Directions for adjacent cells (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes_passed = 0

        # BFS to rot adjacent fresh oranges
        while queue and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
                        
        # If there are still fresh oranges left, return -1; otherwise, return the number of minutes passed.
        return minutes_passed if fresh_count == 0 else -1


if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    solution = Solution()
    print(solution.orangesRotting(grid))
