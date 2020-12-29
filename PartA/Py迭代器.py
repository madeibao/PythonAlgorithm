

iter()函数与next()函数
list、tuple等都是可迭代对象，我们可以通过iter()函数获取这些可迭代对象的迭代器。
然后我们可以对获取到的迭代器不断使用next()函数来获取下一条数据。
iter()函数实际上就是调用了可迭代对象的 __iter__ 方法。



In [1]: li=[1,2,3,4,5,6]

In [2]: li_liter=iter(li)

In [3]: next(li_liter)
Out[3]: 1

In [4]: next(li_liter)
Out[4]: 2

In [5]: next(li_liter)
Out[5]: 3

In [6]: next(li_liter)
Out[6]: 4

In [7]: next(li_liter)
Out[7]: 5

In [8]: next(li_liter)
Out[8]: 6

In [9]: next(li_liter)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-9-efd2732d9495> in <module>()
----> 1 next(li_liter)
