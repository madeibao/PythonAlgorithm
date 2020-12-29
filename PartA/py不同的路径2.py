


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	dp = [[0] * n for _ in range(m)]
    	for i in range(m):
    		d[i][0] = 1

    	for j in range(n):
    		dp[0][j] = 1


    	for i in range(1, m):
    		for j in range(1,n):
    			dp[i][j] = d[i-1][j] + d[i][j-1]

    	return dp[m-1][n-1]


if __name__ == "__main__":
	s =Solution()
	m = 3
	n = 4
	print(s.uniquePaths(m, n))

	