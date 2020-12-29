

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l = 0
        r=len(matrix[0])-1          #注意matrix【0】为中括号
                                    #注意位置 matrix [t,b] [l,r]
        t = 0
        b=len(matrix)-1
        res = []
        while True:
            # 从左到右
            for i in range(l, r+1):         # left to right
                res.append(matrix[t][i])
            # 遍历完成之后会加一，进入下一行。
            t += 1
            if t>b: break

            # 从上到下。
            for i in range(t, b+1):         # top to bottom，此时r为最右
                res.append(matrix[i][r])
            r -= 1
            if l>r: break

            # 从有面到左面
            for i in range(r, l-1, -1):     # right to left，此时b为最下
                res.append(matrix[b][i])
            b -= 1
            if t>b: break


            # 从下面到上面。
            for i in range(b, t-1, -1):      # bottom to top, i赋值b~t,逐渐减小
                res.append(matrix[i][l])

            # l加一，进入另一列。
            l += 1
            if l>r: break
        return res
        
    '''
    注意：以下这种情况，表示只有  res.append这一句是在循环体里的，其他的是和for循环并列的  
            for i in range(l, r + 1): res.append(matrix[t][i])      # left to right
            t += 1
            if t > b: break
    '''

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(matrix))

