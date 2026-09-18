# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 18:33
# @File: enumeratetest

# Python enumerate () 用法

# `enumerate(iterable, start=0)`：**遍历同时拿到索引和元素**，返回迭代器。
#
# - `iterable`：可迭代对象（列表、元组、字符串等）
# - `start`：索引起始值，默认 `0`

lst = ["apple", "banana", "orange"]

if __name__ == '__main__':
    # 默认从0开始
    for idx, val in enumerate(lst):
        print(idx, val)
