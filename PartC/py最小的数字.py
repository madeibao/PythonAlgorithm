

from functools import cmp_to_key

class Solution(object):
	def minnum(self, nums):

		# 首先变成字符串的数组来进行表示
		num2 = list(map(str,nums))
		cmp2 = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
		num2 = "".join(sorted(num2, key=cmp2)).lstrip("0")
		return num2


if __name__ == "__main__":
	s =Solution()
	nums = [10, 2]



