

class Solution(object):
	def unique(self,nums):
		m = len(nums)
		n = len(nums[0])
		dp = [[0]*n  for _ in range(m)]

		if nums[0][0]==0:dp[0][0]=1

		for i in range(m):
			for j in range(n):
				if nums[i][j]==1:
					dp[i][j]= 0
					continue
				if i>0:
					dp[i][j] += dp[i-1][j]
				if j>0:
					dp[i][j] += dp[i][j-1]
		return dp[m-1][n-1]


if __name__ == "__main__":
	s = Solution()
	nums = [[0,0,0],
			[0,1,0],
			[0,0,0],]

	print(s.unique(nums))



