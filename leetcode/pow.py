
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1.0
        if n == 1:
            return x

        if n < 0:
            x = 1 / x
            n = - n

        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
        return 1.0

if __name__ == '__main__':
    x = 2.0
    n = 10
    print(Solution().myPow(x, n))


