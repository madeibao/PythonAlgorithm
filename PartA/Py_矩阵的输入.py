
n = int(input())     # 输入二维数组的行数和列数
line = [[0] * n] * n    # 初始化二维数组
for i in range(n):
    line[i] = input().split(" ")     # 输入二维数组，同行数字用空格分隔，不同行则用回车换行
    line[i] = [int(j) for j in line[i]]     # 将数组中的每一行转换成整型
print(line)         # 打印二维数组

# 二维度的行列式的输入的情况。

# 3
# 2 32 4
# 23 4 4
# 2 3 4
# [[2, 32, 4], [23, 4, 4], [2, 3, 4]]


n = int(input())        # 输入二维数组的行数和列数
line = [[0]*n]*n        # 初始化二维数组
for i in range(n):
    line[i] = input().split(" ")       # 输入二维数组，同行数字用空格分隔，不同行则用回车换行
print(line)


# 这里是按照字符的形式来进行输入的表达。

# 3
# 1 2 3
# 2 3 3
# 22 33 12
# [['1', '2', '3'], ['2', '3', '3'], ['22', '33', '12']]



# 输入一个m行n列的元素

m, n = map(int, input().split())  	 # 这条语句就能够表示输入的句法。

# 在这里M是行数字，N是列数字。
A = m*[0*n]

for i in range(m):
    A[i] = input().split(" ")
    for j in range(n):
        A[i][j] = int(A[i][j])

print(A)


# 2 3
# 1 2 3
# 1 32 3
# [[1, 2, 3], [1, 32, 3]]














#
# 
# @param presentVolumn int整型二维数组 N*M的矩阵，每个元素是这个地板砖上的礼物体积
# @return int整型
#






