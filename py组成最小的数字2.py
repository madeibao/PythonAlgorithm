# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/9/26 8:43
# @File: Test


from functools import cmp_to_key


class Solution(object):
    def minNum(self, nums):
        if len(nums) == 0:
            return ""

        key2 = cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        return "".join(sorted(map(str, nums), key=key2)).lstrip("0")


if __name__ == "__main__":
    s = Solution()
    nums = [10, 2]
    print(s.minNum(nums))




