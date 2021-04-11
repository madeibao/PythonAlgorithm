

class Solution(object):
	def palindrome(self,strs):

		if strs==strs[::-1]:
			return strs

		res = strs[:1]
		def hepler(strs, i,j):
			while i>=0 and j<len(strs):
				if strs[i]==strs[j]:
					i-=1
					j+=1
				else:
					break
			return strs[i+1:j]

		for i in range(len(strs)):
			temp2 = hepler(strs,i,i)
			temp3 = hepler(strs,i,i+1)
			res = max(res, temp2, temp3,key=len)

		return res

if __name__ == '__main__':

	s = Solution()
	str2 = "babad"
	print(s.palindrome(str2))
