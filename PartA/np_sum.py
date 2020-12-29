
import numpy as np

a = np.array([[1, 2],
              [3, 4]])

sum0 = np.sum(a, axis=0)  # 沿着第0个轴，看到的是[1,2]，[3,4]两个向量
sum1 = np.sum(a, axis=1)  # 沿着第1个轴你看到的是[1,3]，[2,4]两个向量
sum2 = np.sum(a, axis=-1)
print(sum0)   # 输出=[4 6]
print(sum1)   # 输出=[3 7]
print(sum2)




"""
[4,6]
[3,7]

"""