

from functools import reduce
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

print(reduce(lambda x,y:x//y, (16,4)))   # 结果为4。

再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

比方说对一个序列求和，就可以用reduce实现：
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#---例子2的情况。
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579










