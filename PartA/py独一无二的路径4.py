


class Solution(object):
	def uniquepath(self,nums):
		m = len(nums)
		n = len(nums[0])

		dp = [[0]* n for _ in range(m)]

		for i in range(m):
			if nums[i][0] !=1:
				dp[i][0] =1
			else:
				break

		for j in range(n):
			if nums[0][j] !=1:
				dp[0][j] =1 
			else:
				break

		for i in range(1, m):
			for j in range(1,n):

				if nums[i][j] ==1:
					dp[i][j] = 0
				else:
					dp[i][j] =dp[i-1][j] +dp[i][j-1]

		return dp[m-1][n-1]


if __name__ == "__main__":
	s = Solution()
	nums = [[0,0,0],
			[0,1,0],
			[0,0,0],]

	print(s.uniquepath(nums))


