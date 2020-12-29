


# 将数组来排列成为最大的数字的和。


from functools import cmp_to_key

class Solution(object):
	def maxNum(self,nums):
		list2 = list(map(str,nums))
		key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
		res = list(sorted(list2, key=key)).strip("0")
		return res

if __name__ == "__main__":
	s =Solution()
	nums= [10, 2]
	print(s.__init__(nums))

