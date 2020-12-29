



class Solution():
	def selectMatrix(self, nums, target):

		m = len(nums)
		n = len(nums[0])-1

		i,j = 0,n

		while i < m and j>=0:
			if nums[i][j] == target:
				return True
			elif nums[i][j]<target:
				i+=1
			else:
				j-=1

		return -1

if __name__ == "__main__":
	s =Solution()

	matrix = [
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	target = 3
	print(s.selectMatrix(matrix, target))


