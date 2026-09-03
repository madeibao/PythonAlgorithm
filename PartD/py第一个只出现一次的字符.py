


class Solution(object):
	def firstChar(self,strs):
		dict2 = {}

		for i in strs:
			dict2[i] = dict2.get(i, 0) + 1

		for k,v in enumerate(strs):
			if dict2.get(v)==1:
				return v
		return -1


if __name__ == "__main__":
	s = Solution()
	str2 ="leetcode"
	print(s.firstChar(str2))




