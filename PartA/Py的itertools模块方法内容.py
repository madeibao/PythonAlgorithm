

1、Python itertools模块combinations(iterable, r)方法可以创建一个迭代器，
返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序。


import itertools

list1 = [1, 3, 4, 5]
list2 = []
for i in range(1, len(list1)+1):
    iter1 = itertools.combinations(list1, i)
    list2.append(list(iter1))
print(list2)




返回结果：
[[(1,), (3,), (4,), (5,)], [(1, 3), (1, 4), (1, 5), (3, 4), (3, 5), (4, 5)], [(1, 3, 4), (1, 3, 5), (1, 4, 5), (3, 4, 5)], [(1, 3, 4, 5)]]