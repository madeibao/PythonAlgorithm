# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/9/星期五 17:10
# @File: moverobot
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        d = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
        ans = []
        for i in range(len(s)):
            ops = s[i:]
            step = 0
            x, y = startPos[0], startPos[1]  # 初始坐标
            for op in ops:
                x, y = x + d[op][0], y + d[op][1]
                if 0 <= x < n and 0 <= y < n:
                    step += 1
                else:
                    break
            ans.append(step)
        return ans


if __name__ == '__main__':
    n = 3
    startPos = [0, 1]
    s = "RRDDLU"
    print(Solution().executeInstructions(n, startPos, s))
