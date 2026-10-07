# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 20:47
# @File: samestr
from builtins import str


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

if __name__ == '__main__':
    str = "abb"
    str2 = "cdd"
    print(Solution().isIsomorphic(str, str2))