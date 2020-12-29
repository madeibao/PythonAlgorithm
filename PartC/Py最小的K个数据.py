a, b = map(int, input().split())
c = list(map(int, input().split()))
c.sort()  # 排序
d = []  
for i in range(b):
    d.append(c[i])
print(' '.join(list(map(str, d))))   # 内容中加入空格的形式。


"""

按照以下的格式进行输入
首先输入a个数据，代表的是所有的输入的数据，从这些数据中选择b个最小的值。
然后c作为要给列表存储这a个数据
d作为输出结果：

5 3
1 2 3 4 5
1 2 3

5个数据里面的最小的三个数据是1 2 3
"""