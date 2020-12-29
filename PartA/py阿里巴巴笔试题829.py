


# 超时的写法。


import itertools
a, b = input().split(" ")
b = int(b)
list2 = list(set(itertools.permutations(a)))
res = []
for i in list2:
    res.append("".join(i))
res2 = []
for i in res:
    res2.append(i.lstrip('0'))
res3 = [int(i) for i in res2]
count = 0
for i in res3:
    if i % b == 0:
        count += 1
print(count)

