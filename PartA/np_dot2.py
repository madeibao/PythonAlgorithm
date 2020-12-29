import numpy as np  

a = np.array([[1, 2, 3, 4],
			  [2, 3, 3, 4],
			  [3, 2, 1, 2],
			  [3, 1, 2, 2],
			  [2, 1, 2, 3],])

b = np.array([1, 4 ,1, 3])
print(np.dot(a, b))
print(np.tanh(np.dot(a, b)))


#  矩阵乘以向量，最后的结果为一个向量。














