


class Solution:
	def NumberOf1(self, n):
	    count = 0
	    while n&0xffffffff != 0:
	        count += 1
	        n = n & (n-1)
	    return count


# 下面的表达式子只是适用于正数的形式。
# 下面的方法只是适用于正数。

class Solution():
	def NumberOf1(self,n):

		print(list(bin(n)))
		list2 = list(bin(n)[2:])
		print(list2)
		return list2.count('1')

if __name__ == "__main__":
	s = Solution()
	print(s.NumberOf1(-15))



