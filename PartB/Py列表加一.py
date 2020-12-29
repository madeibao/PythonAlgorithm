


import itertools
from typing import List

class Solution():
	def plusOne(self,nums):

		num = functools.reduce(lambda x, y: x * 10 + y, digits)
        num += 1
        str2 = str(num)
        list2 = [int(i) for i in str2]
        return list2


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,3]
	print(s.plusOne(list2))

