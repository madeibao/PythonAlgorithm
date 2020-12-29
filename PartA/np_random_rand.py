
import numpy as np

print(np.random.rand())   		# 生成一个随机数。
print(np.random.rand(1))   		# 生成一个随机数。一行的数字。一个数字。
print(np.random.rand(2))   		# 生成一个随机数。一行的数字。两个数字。
print(np.random.rand(2, 3))     # 生成一个随机数。一行的数字。一个矩阵元素。




# 0.5367350118847248
# [0.03970418]
# [0.49114927 0.89884887]
# [[0.13889798 0.21543892 0.31765403]
#  [0.61207086 0.58145016 0.15983259]]




import numpy as np

print(np.random.randn(2, 3))

# np.random.randn(d0,d1,d2……dn) 
# 1 当函数括号内没有参数时，则返回一个浮点数； 
# 2 当函数括号内有一个参数时，则返回秩为1的数组，不能表示向量和矩阵； 
# 3 当函数括号内有两个及以上参数时，则返回对应维度的数组，能表示向量或矩阵； 
# 4 np.random.standard_normal（）函数与np.random.randn()类似，但是np.random.standard_normal（）的输入参数为元组（tuple）. 
# 5 np.random.randn()的输入通常为整数，但是如果为浮点数，则会自动直接截断转换为整数。