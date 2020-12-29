
# 矩阵中来查找一个元素的值。


class Solution():
	def search(self, nums, target):
		if len(nums)==0 or len(nums[0])==0:
			return False

		m = len(nums)
		n = len(nums[0])-1

		i = 0
		j = n
		while i<m and j >= 0:
			if nums[i][j] > target:
				j-=1
			elif nums[i][j] < target:
				i+=1
			else:
				return True
		return False


if __name__ == "__main__":
	s = Solution()
	nums = [
	  [1,   4,  7, 11, 15],
	  [2,   5,  8, 12, 19],
	  [3,   6,  9, 16, 22],
	  [10, 13, 14, 17, 24],
	  [18, 21, 23, 26, 30],
	]
	target = 5

	print(s.search(nums, target))

