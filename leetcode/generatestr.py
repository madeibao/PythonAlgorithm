# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 10:42
# @File: generatestr


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack('', 0, 0)
        return res


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
