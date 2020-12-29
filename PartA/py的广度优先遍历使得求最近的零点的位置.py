


from typing import List
import Collections

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        Q = collections.deque([])
        visited = set()
        # 初始化队列，将所有起始点加入
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        # 将所有相邻节点加入队列
        while Q:
            i, j = Q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix

if __name__ == "__main__":
	s =Solution()
	list2 = [[0,0,0],[0,1,0],[0,0,0]]

	print(s.updateMatrix(list2))




