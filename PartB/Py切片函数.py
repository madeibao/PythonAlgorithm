L=list(range(10))
L1=L[0:3]  #从索引0开始取，直到索引3为止，但不包括索引3
#运行结果：[0, 1, 2]
L2=L[:3]   #如果第一个索引是0，还可以省略
#运行结果：[0, 1, 2]
L3=L[::-2]  #Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片,倒数第一个元素的索引是-1
print(L3)

L4=L[1:8:2] #前8个数，每两个取一个
#运行结果：[1, 3, 5, 7]
print(L4)
L5=L[::-1]  #倒叙取每一个数
#运行结果：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
L6=L[:]     #只写[:]就可以原样复制一个list
#运行结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

