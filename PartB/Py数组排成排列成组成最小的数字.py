# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/10/31 18:31
# @File: Test.py



# 数组的元素来组成最小的元素的值。


from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(a, b):
            return 1 if a + b > b + a else -1

        nums = sorted([str(i) for i in nums], key=cmp_to_key(compare))
        return "".join(nums)


if __name__ == "__main__":
    list2 = [10, 2]
    s2 = Solution()
    print(s2.minNumber(list2))  # 102 



# 只需要简单的进行修改，就能变成数组排列成最大的数字。
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        if not nums:
            return ''
        # 首先是映射成字符串的形式。
        nums = map(str, nums)
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        # lstrip() 方法: 截掉字符串左边的空格或指定字符  0012->12
        res = ''.join(sorted(nums, key=key)).lstrip('0')
        # 000->''
        return res or '0'








