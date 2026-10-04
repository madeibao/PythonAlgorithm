# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/4/星期日 10:52
# @File: legalbracket.py
from typing import List


class Solution:
    def legalbrackets(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        dict2 = {"{": "}", "[": "]", "(": ")"}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif len(stack) > 0 and dict2.get(stack[-1]) == i:
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    print(Solution().legalbrackets("()"))
