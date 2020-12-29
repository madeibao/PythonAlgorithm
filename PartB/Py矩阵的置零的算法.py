

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 代表的是行
        R = len(matrix)

        # 代表的是列。
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return matrix


if __name__ == "__main__":
	s= Solution()

	matrix =[[1,1,1],
		     [1,0,1],
		     [1,1,1],]
	print(s.setZeroes(matrix))





