# 主要是因为python3不支持比较函数，在一些接受key的函数中（例如sorted，min，max，heapq.nlargest，itertools.groupby），
# key仅仅支持一个参数，就无法实现两个参数之间的对比，
# 采用cmp_to_key 函数，可以接受两个参数，将两个参数做处理，比如做和做差，转换成一个参数，就可以应用于key关键字之后。



from functools import cmp_to_key 

L=[9,2,23,1,2]

sorted(L,key=cmp_to_key(lambda x,y:y-x))

输出：
[23, 9, 2, 2, 1]


sorted(L,key=cmp_to_key(lambda x,y:x-y))
输出：

[1, 2, 2, 9, 23]
