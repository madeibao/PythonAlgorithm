# python中是没用switch语句的，这应该是体现python大道至简的思想，python中一般多用字典来代替switch来实现。

from __future__ import division


def jia(x, y):
    print(x + y)


def jian(x, y):
    print(x - y)


def cheng(x, y):
    print(x * y)


def chu(x, y):
    print(x / y)


operator = {'+': jia, '-': jian, '*': cheng, '/': chu}
# 里面的 jia代表的是一个函数，是具体的调用。


def f(x, o, y):
    operator.get(o)(x, y)



f(3, '+', 2)


