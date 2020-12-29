

# 字符串中的第一个不重复的字母所在的位置和对应的字母

class Solution(object):
	def findFirst(self,strs):

		dict2 = {}
		for i in range(len(strs)):
			dict2[i] = dict2.get(strs[i], 0)+1

		for i in range(len(strs)):
			if dict2[i]==1:
				return strs[i], i+1

if __name__=='__main__':
	s = Solution()
	str2 ="mleetcode"
	print(s.findFirst(str2))

