# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 10:20
# @File: AB.py

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return []

if __name__ == '__main__':
    target = 9
    list = [2, 3, 7, 8]
    print(Solution().twoSum(list, target))

    
