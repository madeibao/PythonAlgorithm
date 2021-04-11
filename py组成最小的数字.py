


from functools import cmp_to_key

class Solution(object):
	def minnum(self,nums):

		list2= list(map(str, nums))
		key2 = cmp_to_key(lambda x, y: int(x+y) - int(y+x))
		return "".join(sorted(list2, key = key2)).lstrip("0")


if __name__ == "__main__":
	s=  Solution()
	nums = [10,2,1]
	print(s.minnum(nums))

