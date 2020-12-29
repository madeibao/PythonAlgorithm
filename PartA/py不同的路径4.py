

# 从左上角到右下角的不同的位置上来判断不同的路径和。
class Solution():
    def uniquePaths(self,m, n):

        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

       	for i in range(1, m):
       		for j in range(1, n):
       			dp[i][j] = dp[i-1][j] + dp[i][j-1]
       	return dp[m-1][n-1]

if __name__ == "__main__":
	s =Solution()
	m = 3 
	n = 2
	print(s.uniquePaths(m, n))

# 不同的路径2的算法

class Solution(object):
	def uniquePaths2(self,arrays):
		m = len(arrays)
		n = len(arrays[0])

		dp = [[0]*n for _ in range(m)]

		for i in range(m):
			if arrays[i][0]==0:
				dp[i][0] = 1

		for j in range(n):
			if arrays[0][j]==0:
				dp[0][j] = 1

		for i in range(1, m):
			for j in range(1, n):
				if arrays[i][j] ==0:
					dp[i][j] = dp[i-1][j]+dp[i][j-1]
		return dp[m-1][n-1]


if __name__ == "__main__":
	s =Solution()
	list2 =[[0,0,0],[0,1,0],[0,0,0]]
	print(s.uniquePaths2(list2))


