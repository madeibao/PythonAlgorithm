
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # 初始化
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        
        if n == 1 and m == 1:
            return 1
    
        # 一共八个方向来判断
        # 八个方向分别是：右，下，左，上，右下，左上，右上，左下
        # 眼观六路，耳听八方
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
        set2 = set()
        queue = deque([(0, 0)])
        set2.add((0, 0))
        step = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                if x == m - 1 and y == n - 1:
                    return step
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    # 判断是否越界，并且是否可以走
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in set2:
                        queue.append((nx, ny))
                        set2.add((nx, ny))
            step += 1
        return -1


if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))

