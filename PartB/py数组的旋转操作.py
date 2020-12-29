

class Solution(object):
	def rotate(self,nums,n):
		if not nums:
			return None
		len2 = len(nums)
		n = n%len2

		self.exchange(nums, 0, n-1)
		self.exchange(nums,n,len2-1)
		self.exchange(nums,0,len2-1)

		return nums

	def exchange(self,nums, i, j):

		while i<j:
			temp = nums[i]
			nums[i] = nums[j]
			nums[j] = temp
			i+=1
			j-=1

		return nums


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,3,4,5]
	n = 2

	print(s.rotate(list2,n))
