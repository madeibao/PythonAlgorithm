

class Solution():

	def search(self,nums, target):
		if len(nums)==0 or len(nums[0])==0:
			return False

		i = 0
		j = len(nums[0]) -1
		while i<len(nums) and j>=0:
			if nums[i][j]<target:
				i += 1
			elif nums[i][j]>target:
				j  -= 1
			else:
				return True
		return False 


if __name__ == "__main__":
    matrix = [[1, 3, 15, 17, 19],
              [2, 4, 16, 17, 22],
              [3, 4, 21, 44, 51],
              [6, 7, 18, 29, 36]]
    a = 7
    s = Solution()

    print(s.search(matrix,a))