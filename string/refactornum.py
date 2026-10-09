# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/9/星期五 17:56
# @File: refactornum
from functools import cmp_to_key


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        if num > 0:
            # 正数：升序排序，把第一个非零数提到最前
            digits = sorted(str(num))
            for i in range(len(digits)):
                if digits[i] != '0':
                    # 交换到首位
                    digits[0], digits[i] = digits[i], digits[0]
                    break
            return int(''.join(digits))
        else:
            # 负数：绝对值各位降序排列
            digits = sorted(str(-num), reverse=True)
            return -int(''.join(digits))

if __name__ == "__main__":
    num = 310
    print(Solution().smallestNumber(num))
