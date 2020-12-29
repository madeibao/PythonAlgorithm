给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91 
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

#--------------------------------------------------------------------------------------------------------------------------------

from typing import List
# 下面的自己写的方法内容会出现超时的情况。
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        num = 0
        for i in range(10**n):
            str2 = str(i)
            list2 = [int(i) for i in str2]
            if len(set(list2)) == len(list2):
                num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(2))

#============================================================================

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        f = 9
        i = 2
        while i <= n and i <= 10:
            f = f*(10-i+1)
            res += f
            i += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countNumbersWithUniqueDigits(2))

















