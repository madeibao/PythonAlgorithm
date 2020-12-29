


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)


        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        return matrix


if __name__ == "__main__":
    s = Solution()
    list2 = [[1, 1, 1, ], [1, 0, 1], [1, 1, 1]]
    print(s.setZeroes(list2))
