


from functools import cmp_to_key


class Solution(object):
	def minnum(self, nums):
		list2 = list(map(str, nums))
		key2 = cmp_to_key(lambda a,b:int(a+b)-int(b+a))
		return "".join(list(sorted(list2, key=key2))).lstrip("0")


if __name__ == "__main__":
	s = Solution()
	list2 = [10, 2, 3]
	print(s.minnum(list2))

