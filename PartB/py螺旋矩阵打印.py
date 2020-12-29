

# 给定一个矩阵，顺时针来打印矩阵。
from typing import List, Tuple

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        l, r = 0, len(matrix[0])-1

        t, b = 0, len(matrix)-1

        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t+=1
            if t>b:break

            for i in range(t, b+1):
                res.append(matrix[i][r])
            r-=1
            if l>r:break

            # 
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b-=1
            if t>b:break

            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l+=1
            if l>r:break
        return res


if  __name__ == "__main__":
    s =Solution()
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(nums))


