
from typing import List, Tuple, Optional

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1
        res = []
        while True:

            # 从左面到右面来更新，横坐标不变。
            for i in range(l,r+1): 
                res.append(matrix[t][i])
            t+=1
            if t>b: break

            # 从上面到下面的时间，纵坐标不变。
            for i in range(t, b+1): 
                res.append(matrix[i][r])
            r-=1
            if l>r: break

            # 从右面到左面，横坐标不变。
            for i in range(r, l-1,-1):
                res.append(matrix[b][i])
            b-=1
            if t>b: break

            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l+=1
            if l>r: break
        return res

if __name__ == "__main__":
    s =Solution()
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(nums))


