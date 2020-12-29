

# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py栈的弹入和弹出的顺序2.py
@Time    :   2020/12/23 19:53:27
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""


class Solution(object):
    def order2(self,pushed, popped):

        stack = []
        j = 0

        for x in pushed:
            stack.append(x)
            while stack and j<len(popped) and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return stack==[]


if __name__=='__main__':
    s = Solution()
    pushed = [1,2,3,4,5]
    popped = [1,2,3,4,5]
    print(s.order2(pushed,popped))

