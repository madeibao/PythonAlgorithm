# python2和python3中的range区别
# python2中的range返回的是一个列表  
# python3中的range返回的是一个迭代值 

# for i in range(1,10)在python2和python3中都可以使用
# 但是要生成1-10的列表，就需要用list(range(1,10))
# 注意：range函数返回一个左闭右开（[left,right)）的序列数


print(type(range(10)))
print(list(range(10)))

# <class 'range'>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




python2的写法是返回一个列表。
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

>>>range(10)        # 从 0 开始到 10   #这里是python2的写法。
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




