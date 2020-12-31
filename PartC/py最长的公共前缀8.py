
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py最长的公共前缀8.py
@Time    :   2020/12/28 14:43:17
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for i in  zip(*strs):
            if len(set(i))==1:
                res+=i[0]
            else:
            	break
        return res


if __name__ == "__main__":
    s =Solution()
    list2 = ["flower","flow","flight"]
    print(s.longestCommonPrefix(list2))

