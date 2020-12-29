
from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
    	if not matrix:
    		return

    	row, col = len(matrix), len(matrix[0])
    	table = [[float("inf")]* col for _ in range(row)]

    	# 每一行和每一列的元素来进行计算。
    	for i in range(row):
    		for j in range(col):
    			if matrix[i][j]==0:
    				table[i][j] = 0

    	for i in range(row):
    		for j in range(col):
    			if i-1>=0:
    				table[i][j] = min(table[i-1][j]+1 ,table[i][j])
    			if j-1>=0:
    				table[i][j] = min(table[i][j-1]+1,table[i][j])


    	for i in  range(row-1,-1,-1):
    		for j in range(col-1,-1,-1):
    			if i+1<row:
    				table[i][j] = min(table[i][j], table[i+1][j]+1)
    			if j+1<col:
    				table[i][j] = min(table[i][j], table[i][j+1]+1)
    	return table

if __name__ == "__main__":
	s = Solution()

	list2 = [[0,0,0],
	         [0,1,0],
	         [0,0,0]]
	print(s.updateMatrix(list2))



