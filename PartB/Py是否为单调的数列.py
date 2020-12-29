


# 判断一个数列是否为单调的，不仅仅是严格的单调数列。


class Solution(object):
	def isMonotonic(self, A):
		return self.isIncrease(A) or self.isDecrease(A)

	def isIncrease(self, A):
		return all(A[i]-A[i+1] >= 0 for i in range(len(A)-1))

	def isDecrease(self, A):
		return all(A[i]-A[i+1] <= 0 for i in range(len(A)-1))




if __name__ == "__main__": 
	list2 = [6,5,4,4]

	s = Solution()
	print(s.isMonotonic(list2))

