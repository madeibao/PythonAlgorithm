


2 元素都为真
接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False

In [2]: all([1,0,3,6])
Out[2]: False

In [3]: all([1,2,3])
Out[3]: True




3 元素至少一个为真　
接受一个迭代器，如果迭代器里至少有一个元素为真，那么返回True，否则返回False

In [4]: any([0,0,0,[]])
Out[4]: False

In [5]: any([0,0,1])
Out[5]: True


