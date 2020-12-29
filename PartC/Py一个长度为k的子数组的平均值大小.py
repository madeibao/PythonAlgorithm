



给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

class Solution():
	def findAverage(self, nums, k):
		max2 = sum(nums[:k])		
		temp =max2 
		for i in range(len(nums)-k):
			temp = temp-nums[i]+nums[i+k]
			max = max(max2,temp)
		return max2


if __name__ == "__main__":
	s = Solution()
	print(s.findAverage([1,12,-5,-6,50,3],4))