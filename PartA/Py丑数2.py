
class Solution():
	def isUgly(self,num):
		if num <0:
			return False

		while True:
			last  = num
			if not num%2:
				num >>= 1
			if not num%3:
				num = num//3
			if not num%5:
				num = num//5
			if num==1:
				return True
			if last == num:
				return False

				
if __name__ == "__main__":
	s = Solution()
	print(s.isUgly(15))