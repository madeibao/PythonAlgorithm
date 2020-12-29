'''

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]  #  //这里是一个矩阵。

# 打印矩阵
def printMatrix(m):
    for ele in m:
        for e in ele:
            print('%3d' % e, end='')
        print("\n")


# 转置矩阵
def transformMatrix(m):
    rt = [[] for i in m[0]]    # m[0] 有几个元素，说明原矩阵有多少列。此处创建转置矩阵的行
    for ele in m:
        for i in range(len(ele)):
            # rt[i] 代表新矩阵的第 i 行
            # ele[i] 代表原矩阵当前行的第 i 列
            rt[i].append(ele[i])
    return rt

printMatrix(matrix) # 首先是打印矩阵的
print('-'*40)
printMatrix(transformMatrix(matrix))

'''

# 矩阵的转置。
# ---------------------------------------------------------------------------
# 矩阵的行和列都是相等的值。

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
        
        return matrix


if __name__ == "__main__":
    s =Solution()
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13,14,15,16]]  #  //这里是一个矩阵。
    print(s.rotate(matrix))
