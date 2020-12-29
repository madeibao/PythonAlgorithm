
# 第一种方法内容。

from tkinter import _flatten
a = [[1, 2], [3, 4]]
print(list(_flatten(a)))

# 第二种方法内容

from itertools import chain
a = [[1, 2], [3, 4]]
print(list(chain.from_iterable(a)))


# 第三种方法，推荐使用的方法内容。
ab = [[1,2,3], [5,8], [7,8,9]]
print([i for item in ab for i in item])  # 一行代码解决的问题。

#================================================================

一维列表转化为二维列表


a = [1,2,3,4]
b = [0,2,4,6]
c = list(zip(a,b))
print(c)

















