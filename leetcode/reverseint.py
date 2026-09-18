# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 10:29
# @File: reverseint
import signal


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        maxNum = 2 ** 31 - 1
        minNum = -2 ** 31
        sig = 1
        if x < 0:
            sig = -1
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x //= 10
            if sig == 1 and res > maxNum:
                return 0
            elif sig == -1 and -res < minNum:
                return 0
        return sig * res


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
