
# 指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。

# 输入：Y = 1992, M = 7
# 输出：31
#================================================================

from typing import List

class Solution():
    def numberOfDays(self, Y: int, M: int) -> int:
        D = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if Y % 400 == 0 or Y % 4 == 0 and Y % 100 != 0:
            D[1] += 1
        return D[M]


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfDays(1995, 8))









