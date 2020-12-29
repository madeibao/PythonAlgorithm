

# 判断是否为特殊的矩阵
# 从左上角的右下角的位置的数字都相同。


from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)
        y = len(matrix[0])

        if x==1 or y==1 return True

        for i in range(x-1):
            for j in range(y-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True

        

if __name__ == "__main__":
    s =Solution()
    matrix = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]]
    print(s.isToeplitzMatrix(matrix))

