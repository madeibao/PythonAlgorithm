

from typing import List
from functools import cmp_to_key

class Solution():
	def minNum(self,nums):
		def compare(a,b):
			return 1 if a+b>b+a else -1
		nums = sorted([str(i) for i in nums], key=cmp_to_key(compare))

		return "".join(nums)

if __name__ == "__main__":
	list2= [10, 2]
	s = Solution()
	print(s.minNum(list2))

	