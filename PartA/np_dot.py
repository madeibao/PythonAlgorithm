import numpy as np
a = np.array([1, 2, 3])      # shape: (3,)
b = np.array([1, 2, 3])      # shape: (2,)
c = np.dot(a, b)             # 通过a[:, None]来增加一个维度，将a的shape变为（3，1）, b:（1，2）
print(c)




# 结果为14.
		 [1

[1,2,3]   2      = 1*1+2*2+3*3=14

		  3]


















