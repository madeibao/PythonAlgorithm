# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 21:40
# @File: toHex


class Solution:
    def toHex(self, num: int) -> str:
        alphabet = "0123456789abcdef"
        ret = []
        for _ in range(8):
            ret.append(num % 16)
            num //= 16
            if num == 0:
                break
        return "".join(alphabet[n] for n in ret[::-1])


if __name__ == "__main__":
    print(Solution().toHex(-1))
    print(Solution().toHex(0))
