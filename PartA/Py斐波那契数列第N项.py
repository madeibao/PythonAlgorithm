

class Solution:
    def Fibonacci(self, n):        # write code here
        res = [0, 1, 1, 2]
        while len(res)<= n:
            res.append(res[-1]+res[-2])
        return res[n]


b = Solution()
num = int(input())
print(b.Fibonacci(num))










