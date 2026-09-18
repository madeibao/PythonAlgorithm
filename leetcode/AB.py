# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 10:20
# @File: AB.py

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        dicta = {}
        for i in range(len(nums)):
            if target - nums[i] in dicta:
                return [dicta[target - nums[i]], i]
            dicta[nums[i]] = i
        return []

if __name__ == '__main__':
    target = 9
    list = [2, 3, 7, 8]
    print(Solution().twoSum(list, target))

    
