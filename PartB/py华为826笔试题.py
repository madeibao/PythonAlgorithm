# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/6/9 9:21
# @File: Test.py

# 2020.8.26 华为笔试题目：
# -*- conding: utf-8 -*-

from typing import List

# 两两交换数字
def fun2(list2):
    res = []
    for i in range(0, len(list2)-1, 2):
        res.append(list2[i+1])
        res.append(list2[i])
    return res


# 填充
def fun3(n):
    return bin(n)[2:].rjust(32, '0')


list2 = list(map(int, input().split(" ")))
res = []
for i in list2:
    res.append("".join(fun2(list(fun3(i)))))

temp = "".join(res)
temp2 = temp[-2:]+temp[:-2]


res2 = []
while len(temp2) > 0:
    res2.append(temp2[:32])
    temp2 = temp2[32:]

res3 = []
for i in range(len(res2)):
    res3.append(int(res2[i], 2))

print(" ".join(map(str, res3)))
































