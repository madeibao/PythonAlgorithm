
import numpy as np
ar1 = np.array([[1, 2, 3],
                [4, 5, 6]])
ar2 = np.array([[7, 8, 9],
                [11, 12, 13]])

# 水平拼接，沿着行的方向，对列进行拼接
print(np.column_stack((ar1, ar2)))


# 垂直拼接，沿着列的方向，对行进行拼接每次都是行首先变化。
print(np.row_stack((ar1, ar2)))


"""
结果：

[[ 1  2  3  7  8  9]
 [ 4  5  6 11 12 13]]
 
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [11 12 13]]


"""