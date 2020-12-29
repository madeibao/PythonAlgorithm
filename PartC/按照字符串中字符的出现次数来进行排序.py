
from collections import Counter

class Solution(object):
	def frequencySort(self,s):
		dic2 = Counter(s)
		dict2 = sorted(dic2.items(), key=lambda x:x[1], reverse=True)
		return "".join(list(map(lambda x:x[0]*x[1], dict2)))


if __name__ == "__main__":
	s =Solution()
	str2 ="leetcode"
	print(s.frequencySort(str2))


