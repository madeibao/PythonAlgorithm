
from functools import cmp_to_key

class Solution(object):
	def minNum(self,nums):

		if not nums:
			return 0
		list2 = list(map(str,nums))	
		key2 = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
		return "".join(sorted(list2, key=key2)).lstrip("0")

if __name__ == "__main__":
	s = Solution()
	list2 = [20, 3, 2, 1]
	print(s.minNum(list2))

	
