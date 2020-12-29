
'''

题目
编程题1.
输入一个N阶方阵（0<N<10），输出此方阵的顺时针旋转M次（0<=M<=1000）次后的方阵。

输入：
N #一个数，代表接下来是几阶矩阵
矩阵 #N行 N列， 空格隔开
M #旋转次数

要求输出：
旋转后的N阶矩阵，每行内数字用空格隔开

Python代码：
解法1： 使用内置函数 rot90()
解法2： 利用矩阵乘法，左乘或者右乘一个负对角线为-1的矩阵
解法3： 利用索引
我在上机测试的时候因为调整输入输出浪费了一些时间，就采用了最简单的第一种方法。
————————————————
版权声明：本文为CSDN博主「洛小花花」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_42159183/article/details/90171421

# =====----------------------------------------------------------------
# ----------------------------------------------------------------------------------
'''

import numpy

n = int(input())

matrix=[]
for i in range(n):
    matrix.append([])
    matri = input().split()
    for j in range(n):
        matrix[i].append(int(matri[j]))
matrix = np.array(matrix)

roll = int(input())
roll = roll%4

new_matrix = np.rot90(matrix,-roll)

for i in range(len(new_matrix)):
    for j in range(len(new_matrix)-1):
        print(new_matrix[i][j],end=' ')
    j = j+1
    print(new_matrix[i][j])
