





class Solution(object):
	def maxScore(self,s):
		res = 0

		for i in range(1, len(s)):
			temp = s[:i].count('0') + s[i:].count('1')
			res = max(res,temp)

		return res

if __name__ == '__main__':
	s = Solution()
	print(s.maxScore("011101"))

