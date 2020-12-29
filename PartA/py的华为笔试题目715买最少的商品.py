

class Solution():
    def exchange(self, coins, n):
        dp = [-1 for i in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    if dp[i]==-1 or dp[i]>dp[i-coin]+1:
                        dp[i] = dp[i-coin] +1
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    count = list(map(int, input()))

    print(s.exchange(n, count))
