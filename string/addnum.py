# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/7/星期三 22:15
# @File: addnum
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 10))
            carry = total // 10
        return ''.join(reversed(res))


if __name__ == "__main__":
    solution = Solution()
    a = "13"
    b = "27"
    print(solution.addBinary(a, b))
