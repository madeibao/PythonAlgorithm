

# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py全排列.py
@Time    :   2020/12/31 14:24:06
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""


class Solution(object):
    def permutations(self,nums):

        res = []
        def helper(start):
            if start==len(nums):
                res.append(nums[:])
            for i in range(start, len(nums)):
                nums[i],nums[start] = nums[start], nums[i]
                helper(start+1)
                nums[i],nums[start] = nums[start], nums[i]

        helper(0)
        return res

if __name__ == "__main__":
    s =Solution()
    nums = [1,2,3]
    print(s.permutations(nums))

