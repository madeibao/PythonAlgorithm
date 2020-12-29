
# 所谓冤家数字，指的就是由仅仅由两个数字组合称的数字，按照从小到大的顺序进行排列。

例如  2与4组成的冤家数字。


[2, 4, 22, 24, 42, 44, 222, 224, 242, 244, 422, 424, 442, 444, 2222, 2224, 2242, 2244, 2422, 2424, 2442, 2444, 4222, 4224, 4242, 4244, 4422, 4424, 4442, 4444]


import itertools
import functools

print("请输入两个数字")
a, b = map(int, input().split(","))
str2 = str(a)+str(b)
list2 = []
for i in range(1, 5):
    for x in itertools.product(str2, repeat=i):
        x = list(x)
        list2.append(x)

list3 = []

for i in list2:
    list4 = list(map(int, i))
    num = functools.reduce(lambda x, y: x * 10 + y, list4)
    list3.append(num)

print(list3)
