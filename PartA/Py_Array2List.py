import numpy as np

a1 = [[1, 2, 3], [4, 45, 5]]
a2 = np.asarray(a1)  # 列表到矩阵。
print(a2)
a3 = a2.tolist()     # 矩阵到列表。
print(a3)



[[ 1  2  3]
 [ 4 45  5]]
[[1, 2, 3], [4, 45, 5]]


