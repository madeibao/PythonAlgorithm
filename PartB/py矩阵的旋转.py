


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        先做矩阵转置（即沿着对角线翻转），然后每个列表翻转；
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for m in matrix:
            m.reverse()
    
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        通过内置函数zip，可以简单实现矩阵转置，下面的代码等于先整体翻转，后转置；
        不过这种写法的空间复杂度其实是O(n);
        """
        matrix[:] = map(list, zip(*matrix[::-1]))

if __name__ == "__main__":
	s = Solution()
	