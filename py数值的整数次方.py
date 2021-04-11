

# 给定数值和幂，求一个整数的幂，幂指数也可以为负数。

class Solution(object):
	def mypow(self,num,k):

		if k==0:return 1
		if k==1:return num

		if k<0:
			num = 1/num
			k = -k

		temp = self.mypow(num,k//2)
		if k%2==1:
			return num*temp*temp
		else:
			return temp*temp


if __name__ == "__main__":
	s= Solution()
	num = 3
	k = -2	
	print(s.mypow(num,k))

