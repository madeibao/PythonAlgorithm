# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 10:43
# @File: countwords


class Solution:
    def countSegments(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        list = s.split()
        return len(list)

if __name__ == '__main__':
    sol = Solution()
