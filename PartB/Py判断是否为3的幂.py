
class Solution:
    def isPowerOfThree(self, n) -> bool:
        res = 1
        while res < n:
            res *= 3
        return res == n


num = int(input())
cc = Solution()
print(cc.isPowerOfThree(num))















