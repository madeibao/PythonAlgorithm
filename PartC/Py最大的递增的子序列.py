
题目：这种序列可以是不连续的。

给定一串数组，返回其中的最长递增子序列的长度。例如：给定数组[10, 9, 2, 5, 3, 7, 101, 18],
则其最长递增子序列为[2, 3, 7, 101],返回长度4.

解题思路：
使用动归。用Dp[i]来保存从0-i的数组的最长递增子序列的长度。
如上数组Dp[0]=1,Dp[1]=1,Dp[2]=1,Dp[3]=2,Dp[4]=2。。。
计算Dp[i]的值可以对Dp[i]之前数值进行遍历，如果nums[i]>nums[j],则Dp[i] = max(Dp[i],Dp[j]+1)。复杂度为O(n*n)


class Solution():
	def getIncrease(self, A):
		if len(A) ==0:
			return 0
		N = len(A)
		Dp = [1]*N
		for i in range(N-1):
			for j in range(0,i+1):
				if(A[i+1]>A[j]):
					Dp[i+1] = max(Dp[i+1],Dp[j]+1)
		
		return max(Dp)


if __name__ == "__main__":
	s= Solution()
	print(s.getIncrease[10, 9, 2, 5, 3, 7, 101, 18])


# 另一种算法思路：

class Solution():
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        ans = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

