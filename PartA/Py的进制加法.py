

# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/6/9 9:21
# @File: Test.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(n, x):

    # n为待转换的十进制数，x为机制，取值为2-16
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',]
    b = []
    while True:
        s = n//x  # 商
        y = n % x  # 余数
        b = b+[y]
        if s==0:
            break
        n = s
    b.reverse()   # 逆序。
    for i in b:
        print(a[i], end='')

print(f(15,2))

