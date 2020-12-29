a = [1,3,5,7,9]
b = [2,4,6,8,0]
print(map(lambda x, y: x+y, a, b))
[3, 7, 11, 15, 9]


# 以上的输出是python2.7的版本。


# 对于python3的版本。
# 要添加list转化成列表的形式进行输出。



a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 0]
print(map(lambda x,y: x + y, a, b))
<map object at 0x7f53640e3588>      		# 这里返回的是一个对象。
print(list(map(lambda x,y: x + y, a, b)))   # 只有转变成为list之后才能变成列表的形式。

# 结果为：[3, 7, 11, 15, 9]



