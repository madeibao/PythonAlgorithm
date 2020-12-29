

# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 输入: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4
#================================================================


from typing import List

class Solution(object):

    def maximalSquare(self, matrix):

        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0
        # 矩阵的行数
        row = len(matrix)
        # 矩阵的列数
        col = len(matrix[0])

        size = [[0] * col for i in matrix]
        res = 0

        # 代表的是行
        for i in range(row):
            # 代表的是列的内容。
            for j in range(col):
                if col == 0:
                    size[i][j] = int(matrix[i][j])
                else:
                    size[i][j] = min(size[i-1][j], size[i][j-1], size[i-1][j-1]) + 1 if int(matrix[i][j]) else 0
                res = max(res, size[i][j])
        return res**2


if __name__ == "__main__":

    s = Solution()
    matrix  = [[1,0,1,0,0],
               [1,0,1,1,1],
               [1,1,1,1,1], 
               [1,0,0,1,0],]

    print(s.maximalSquare(matrix))
