

# 判断一个数字是否为丑数。
class Solution(object):
	def uglyNum(self, num):
		if num<1:
			return False
		while num%5==0:
			num /= 5
		while num%3==0:
			num /= 3
		while num%2==0:
			num/= 2

		return num==1


if __name__=='__main__':
	s = Solution()
	print(s.uglyNum(14))
