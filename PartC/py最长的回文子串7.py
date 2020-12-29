
class Solution(object):
	def palindrome(self,strs):
		if strs==strs[::-1]:
			return strs


		def helper(s, i,j):

			while i>=0 and j<len(s):
				if s[i]==s[j]:
					i-=1
					j+=1
				else:
					break

			return s[i+1:j]

		res =strs[:1]
		for i in range(len(strs)):
			temp2 = helper(strs, i,i)
			temp3 = helper(strs, i,i+1)

			res = max(res, temp2, temp3, key=len)
		return res 

if __name__ == "__main__":
	s = Solution()
	print(s.palindrome("babad"))

	