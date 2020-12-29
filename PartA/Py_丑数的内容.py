

# 首先判断是否为丑数的内容
# 然后给出第几个丑数的结果值。



from typing import List

'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i, num = 0, 1
        uglys = list()

        while i < n:
            if self.isugly(num):
                uglys.append(num)
                i += 1
            num += 1

        return uglys[n-1]

    
    def isugly(self, n: int) -> bool:   
        for p in [2, 3, 5]:
            while n and n%p==0:
                n = n//p
        return n==1

'''

# ----------------------------------------------------------------
# 方法2的内容

# class Solution():
#     ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))
#     def nthUglyNumber(self, n: int) -> int:
#         return self.ugly[n - 1]

# ----------------------------------------------------------------
# 方法3的内容。

# import heapq
# class Solution():
#     def nthUglyNumber(self, n: int) -> int:
#         q = [1]
#         for _ in range(1, n):
#             val = heapq.heappop(q)
#             while q and q[0] == val:
#                 heapq.heappop(q)
#             for i in [2, 3, 5]:
#             	heapq.heappush(q, i*val)
#         return q[0]

#==============================================================


class Solution():
    def nthUglyNumber(self, n: int) -> int:

    	# 首先初始化一个长度内容的列表。
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]

# 输入一个数字，第n个丑数
if __name__ == "__main__": 

    s = Solution()
    num = int(input())
    print(s.nthUglyNumber(num))
