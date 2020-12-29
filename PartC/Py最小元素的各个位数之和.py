
# 给你一个正整数的数组 A。
# 然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。
# 最后，假如 S 所得计算结果是 奇数 的请你返回 0，否则请返回 1。
#================================================================



class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, s = min(A), 0
        while n > 0:
            n, tmp = divmod(n, 10)
            s += tmp
        return 1 - s % 2


if __name__ == "__main__":
    s =Solution()
    nums = [99,77,33,66,55]
    print(s.sumOfDigits(nums))