


# 数组来组成的最小的数字的值。


from functools import cmp_to_key

class Solution(object):
	def minnum(self,nums):

		list2 = list(map(str, nums))
		cmp2 = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
		return "".join(sort(list2,key=cmp2)).lstrip("0")



if __name__ == "__main__":
	s = Solution()
	print(s.minnum([10,2]))
