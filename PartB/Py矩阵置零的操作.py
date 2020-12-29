
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        column=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for j in column:
            for i in range(len(matrix)):
                matrix[i][j]=0
        return



if __name__ == "__main__":
	s = Solution()
	list2 = [[1,1,1],[1,0,1],[1,1,1]]
	s.setZeroes(list2)
	print(list2)
	
