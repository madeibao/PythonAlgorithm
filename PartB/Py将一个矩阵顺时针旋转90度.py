# 4*4矩阵旋转90度

# 例如输入：

4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16


#输出

13 9 5 1
14 10 6 2
15 11 7 3
16 12 8 4
#===================================================================


try:
    while 1:
        n = int(input())
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().split())))
        for i in range(n//2):
            mat[i], mat[n-1-i] = mat[n-1-i], mat[i]
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n):
            print(' '.join(map(str, mat[i])))
except:
    pass