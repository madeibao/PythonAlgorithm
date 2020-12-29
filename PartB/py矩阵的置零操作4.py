

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setA = set()
        setB = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			setA.add(i)
        			setB.add(j)

       	for i in range(m):
       		for j in range(n):
       			if i in setA or j in setB:
       				matrix[i][j] = 0

       	return matrix

if __name__ == "__main__":
	s = Solution()
	list2 = [[1,1,1],
			 [1,0,1],
			 [1,1,1]]

	print(s.setZeroes(list2))

