

class Solution(object):
	def generate(self, n):
		self.res= []

		def helper(str2, left, right):
			if left>right:
				return 	
			if left==0 and right == 0:
				self.res.append(str2)
				return

			if left<0 or right<0:
				return

			helper(str2+"(",left-1,right)
			helper(str2+")",left,right-1)

		# 调用模型，选出最终的结果值
		helper("",n,n)
		return self.res

if __name__ == '__main__': 
	s = Solution()
	n = 3
	print(s.generate(n))

