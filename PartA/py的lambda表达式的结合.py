

# 第一个map函数的内容。

>>> list(map(lambda x:x*2,range(1,10)))
[2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> list(map(lambda x, y: x*y, range(1,10), range(2, 11)))
[2, 6, 12, 20, 30, 42, 56, 72, 90]
>>> list(map(lambda x: 1, range(1,10)))

[1, 1, 1, 1, 1, 1, 1, 1, 1]


#------------------------------------------------------------------------------------------------
# filter 函数和lambada函数的相互的结合。

>>> list(filter(lambda x:x>10, range(1,20)))
[11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> list(filter(lambda s: s != 'a', 'abcdefg'))
'bcdefg'


def add2(x):
    return x>3

print(list(filter(lambda x: add2(x), [1, 2, 3, 4, 5, 6, 7, 8])))


#------------------------------------------------------------------------------
# reduce 函数和lambda函数相互的结合

>>> list(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
15
# 内部执行过程，((((1+2)+3)+4)+5)

# list只有一个元素
>>> list(reduce(lambda x: x+2, [1]))
1

#reduce 如果list的长度大于1，lambda表达式必须有两个参数（大于2个参数是不对的）
>>> reduce(lambda x: x+2, [1, 2, 3, 4, 5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes exactly 1 argument (2 given)


#----------------------------------------------------------------


