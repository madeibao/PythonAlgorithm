# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 14:52
# @File: maxnum

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums is None or len(nums) == 0:
            return ''
        list2 = map(str, nums)
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        res = ''.join(sorted(list2, key=key))
        return "0" if res[0] == "0" else res

if __name__ == '__main__':
    sol = Solution()
    list = [20, 1]
    print(sol.largestNumber(list))
