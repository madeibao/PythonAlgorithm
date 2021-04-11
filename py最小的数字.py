
from functools import cmp_to_key

class Solution(object):
	def minnum(self,nums):

		if len(nums)==0:
			return ""
		key2 = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
		return "".join(sorted(list(map(str,nums)))).lstrip("0")


if __name__ == '__main__': 
	s  = Solution()
	nums = [10,2,2]
	print(s.minnum(nums))
