# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/1/星期四 15:10
# @File: sumfour
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        dict = {}
        for a in nums1:
            for b in nums2:
                if a + b in dict:
                    dict[a + b] += 1
                else:
                    dict[a + b] = 1

        count = 0
        for c in nums3:
            for d in nums4:
                temp = - c - d
                if temp in dict:
                    count += dict[temp]
        return count


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))
