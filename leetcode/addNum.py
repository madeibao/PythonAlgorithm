# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 11:09
# @File: addNum


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return list(map(int, str(num)))


if __name__ == '__main__':
    digits = [1, 0]
    print(Solution().plusOne(digits))
