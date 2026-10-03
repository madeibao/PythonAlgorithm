# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 15:45
# @File: buddystring

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        index = []
        if len(s) != len(goal):
            return False

        if len(s) == len(goal):
            for i in range(len(s)):
                if s[i] != goal[i]:
                    index.append(i)

        if (
                len(index) == 2
                and s[index[0]] == goal[index[1]]
                and s[index[1]] == goal[index[0]]
        ):
            return True

        if len(index) == 0 and len(s) - len(set(s)) > 0:
            return True
        return False
