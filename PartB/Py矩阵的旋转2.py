



# 矩阵顺时针来旋转90度


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        for i in range(N):
            for j in range(i, N, 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N):
            matrix[i].reverse()


if __name__ == "__main__":
	s =Solution()

	matrix = [
	  [1,2,3],
	  [4,5,6],
	  [7,8,9],
	]
	s.rotate(matrix)

	print(matrix)

