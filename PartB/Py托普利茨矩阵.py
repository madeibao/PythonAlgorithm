如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是托普利茨矩阵。

给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。

示例 1:

输入: 
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
输出: True
解释:
在上述矩阵中, 其对角线为:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。
各条对角线上的所有元素均相同, 因此答案是True。



from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)   # 代表行数  3
        y = len(matrix[0])   # 代表列数  4

        if x == 1 or y == 1: return True
        for i in range(x-1):
            for j in range(y-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2],
    ]
    print(s.isToeplitzMatrix(matrix))


