


class Solution(object):
	def sumPath(self, nums):

		m = len(nums)
		n = len(nums[0])

		if m<1:
			return 0
		if n<1:
			return 0

		# 如果第一个位置就堵在一起的话，结果为0.
		if nums[0][0]==1:
			return 0
		dp = [[0]*n for _ in range(m)]

		for i in range(m):
			for j in range(n):

				if i==0 and j==0:
					dp[i][j] =1
				elif i==0 and j!=0:
					if nums[i][j]==0:
						dp[i][j] = dp[i][j-1];
				elif i!=0 and j==0:
					if nums[i][j]==0:
						dp[i][j] = dp[i-1][j]
				else:
					if nums[i][j]==0:
						dp[i][j] = dp[i-1][j] + dp[i][j-1]

		return dp[-1][-1]


if __name__ == "__main__":
	s =Solution()
	list2= [[0,0,0],[0,1,0],[0,0,0]]

	print(s.sumPath(list2)) #


#----------------------------------------------------------------
# ------------------------------------------------------------
