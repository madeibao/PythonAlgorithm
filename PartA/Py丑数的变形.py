

class Solution():
    def nthUglyNumber(self, n: int) -> int:

    	# 首先初始化一个长度内容的列表。
        dp = [0] * n
        dp[0] = 1
        l_3 = 0
        l_5 = 0
        l_7 = 0
        for i in range(1, n):
            dp[i] = min(3 * dp[l_3], 5 * dp[l_5], 7 * dp[l_7])
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
            if dp[i] >= 7 * dp[l_7]:
                l_7 += 1
        return dp[-1]

# 输入一个数字，第n个丑数
if __name__ == "__main__": 

    s = Solution()
    num = int(input())
    print(s.nthUglyNumber(num))
