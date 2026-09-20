# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 11:09
# @File: addNum
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return list(map(int, str(num)))


if __name__ == '__main__':
    digits = [1, 0]
    print(Solution().plusOne(digits))
