

# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py旋转数组的最小值.py
@Time    :   2020/12/30 21:36:15
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   旋转数组的最小值。
"""

class Solution(object):
    def spiralOrder(self,nums):
        
        i,j = 0,len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[mid]>nums[j]: 
                i = mid+1
            elif nums[mid]<nums[j]:
                j = mid
            else:
                j = j-1

        return nums[i]


if __name__ == "__main__":
    s = Solution()
    nums = [3,4,5,6,7,7,1,2]
    print(s.spiralOrder(nums))
    




