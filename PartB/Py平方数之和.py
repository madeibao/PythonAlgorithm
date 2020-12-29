# 给定一个数字，判断是否存在两个数字的平方和等于这个数字
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5


双指针的解法。



import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        j = int(math.sqrt(c))
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False