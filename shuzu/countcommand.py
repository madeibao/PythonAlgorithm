

class Solution:
    def countCommas(self, n: int) -> int:
        """
        统计 1 到 n 之间数值大于 999 的整数个数

        Args:
            n: 统计上界，统计范围为闭区间 [1, n]

        Returns:
            区间内大于 999 的整数个数
        """
        cnt = 0
        for a in range(1, n+1):
            if a>999:
                cnt += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    n = 1000000
    print(sol.countCommas(n))