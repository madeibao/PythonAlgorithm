
.# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py最长的公共前缀5.py
@Time    :   2020/12/28 14:43:24
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""



class Solution():
    def mostCommon(self,strs):
        str2 =""

        for i in zip(*strs):
            if len(set(i))==1:
                str2+=i[0]
        return str2


if __name__=='__main__':
    list2 = ["apple", "applist","append","appmmm"]
    s = Solution()
    print(s.mostCommon(list2))