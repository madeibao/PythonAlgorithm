


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        while n:
            res += n // 5
            n = n // 5
        return res

if __name__ == '__main__':
    n = 10
    print(Solution().trailingZeroes(n))

