


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n//2):
            for j in range(n):
                matrix[j][i], matrix[j][n-i-1] = matrix[j][n-i-1], matrix[j][i]
        return matrix

if  __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],
     [4,5,6],
     [7,8,9]
    ]
    print(s.rotate(matrix))

    
