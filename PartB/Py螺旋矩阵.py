
'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ],
]

'''
#==================================================================
from typing import List


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for i in range(n)] for j in range(n)]
        c, j = 1, 0
        while c <= n*n:
            # 从左向右
            for i in range(j, n-j):
                array[j][i] = c
                c += 1
            # 从上往下走
            for i in range(j+1, n-j):
                array[i][n-j-1] = c
                c += 1
            # 从右往左走
            for i in range(n-j-2, j-1, -1):
                array[n-j-1][i] = c
                c += 1
            # 从下往上走
            for i in range(n-j-2, j, -1):
                array[i][j] = c
                c += 1
            j += 1   # j用来进行循环的指针的变化情况。
        return array


if __name__ == '__main__':
    s = Solution()
    array2 = s.generateMatrix(4)

    for i in array2:
        for j in i:
            print(j, end=" ")
        print("\n")




