# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/2/星期五 21:51
# @File: gettax.py

class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        result = 0
        prev = 0
        for u, v in brackets:
            if income > u:
                result += (u - prev) * v / 100
            else:
                result += (income - prev) * v / 100
                return result
            prev = u
        return result


if __name__ == "__main__":
    brackets = [[3, 50], [7, 10], [12, 25]]
    income = 10
    print(Solution().calculateTax(brackets, income))
