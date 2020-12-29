


class Solution(object):
	def countSubString(self, s):

		count = 0

		for i in range(len(s)):
			for j in range(i+1,len(s)+1):
				 if s[i:j] ==s[i:j][::-1]:
				 	count += 1 

		return count 

if __name__ == "__main__":
	s = Solution()
	str2 ="abc"
	print(s.countSubString(str2))

	