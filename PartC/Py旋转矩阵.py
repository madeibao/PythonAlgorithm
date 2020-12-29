

# 矩阵的顺时针的旋转的过程

# 原始的矩阵
#----------------------------------------------------------------
#[
#		[1,2,3],
##		[4,5,6],
#		[7,8,9],
#]

#================================
# [[7, 4, 1], 
#  [8, 5, 2], 
#  [9, 6, 3]]


#----------------------------------------------------------------


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
            	# 核心的关键代码
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new
        return matrix



if __name__ == "__main__":
	s = Solution()
	list2 = [
		[1,2,3],
		[4,5,6],
		[7,8,9],
	]

	print(s.rotate(list2))



