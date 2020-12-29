import numpy as np

# """
# array和asarray都可以将结构数据转化为ndarray，
# 但是主要区别就是当数据源是ndarray时，array仍然会copy出一个副本，占用新的内存，但asarray不会。
# asarray 并不会暂用新的内存的空间。
# """

arr1 = np.ones((3, 3))
arr2 = np.array(arr1)
arr3 = np.asarray(arr1)
arr1[1] = 2

print('arr1:\n', arr1)
print('arr2:\n', arr2)
print('arr3:\n', arr3)





# arr1:
#  [[1. 1. 1.]
#  [2. 2. 2.]
#  [1. 1. 1.]]
# arr2:
#  [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
# arr3:
#  [[1. 1. 1.]
#  [2. 2. 2.]
#  [1. 1. 1.]]
