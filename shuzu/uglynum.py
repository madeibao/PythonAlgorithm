

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(x: int) -> bool:
            return x // a + x // b + x // c - x // lcm_ab - x // lcm_ac - x // lcm_bc + x // lcm_abc >= n

        def lcm(x: int, y: int) -> int:
            """
            计算两个整数的最小公倍数。

            Args:
                x: 第一个整数
                y: 第二个整数

            Returns:
                两个整数的最小公倍数
            """
            from math import gcd
            return x * y // gcd(x, y)

        def gcd(x: int, y: int) -> int:
            """
            使用欧几里得算法（辗转相除法）计算两个整数的最大公约数。

            Args:
                x: 第一个整数
                y: 第二个整数

            Returns:
                两个整数的最大公约数
            """
            if y == 0:
                return x
            return gcd(y, x % y)

        lcm_ab = lcm(a, b)
        lcm_ac = lcm(a, c)
        lcm_bc = lcm(b, c)
        lcm_abc = lcm(lcm_ab, c)

        l, r = 1, n * min(a, b, c)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l

if __name__ == "__main__":
    a = 12
    b = 15
    c = 20
    n = 10
    print(Solution().nthUglyNumber(n, a, b, c))