

# 暴力方法来进行破解
# 美团829笔试题的第四题的解法。

'''
5 5
4 1 4 1 2
10
'''

#-------------------------------------------------------------------------------------------------------------

from itertools import combinations


def strictly_decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))

a, b = map(int, input().split(" "))
list2 = list(map(int, input().split(" ")))

res = []
for i in range(1, b+1):
    res.append(list(combinations(list2, i)))

res2 = []
for i in res:
    for j in i:
        res2.append(list(j))
count = 0
for i in res2:
    if strictly_decreasing(i):
        count += 1
print(count)

