# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py完数.py
@Time    :   2020/11/24 22:21:59
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""
def wanshu():
    result=[]
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            result.append(i)
    return result
    
 
print(wanshu())


