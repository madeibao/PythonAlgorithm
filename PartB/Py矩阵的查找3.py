
from typing import List



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    	m = len(matrix)
    	n = len(matrix[0])-1

    	i=0
    	j = n

    	# 从右上角的位置来进行查找。
    	while i<m and n>=0:
    		if matrix[i][j] > target:
    			j-=1
    		elif matrix[i][j] < target:
    			i+=1
    		else:
    			return True
    	return False


if __name__ == "__main__":


	s =Solution()
	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 3

	print(s.searchMatrix(matrix, target))

	

