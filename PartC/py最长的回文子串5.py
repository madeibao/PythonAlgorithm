
# 最长的回文子串的值



class Solution:
    def longestPalindrome(self, s: str) -> str:

    	def helper(str2, left, right):
    		while left>=0 and right<len(str2) and str2[left]==str2[right]:
    				left-=1
    				right+=1
    		return str2[left+1:right]

    	res =s[:1]
    	for i in range(len(s)):
    		str2 = helper(s,i,i)
    		str3 = helper(s,i,i+1)
    		res = max(res, str2, str3,key=len)
    	return res


if __name__=='__main__':
	s =Solution()
	str2="babad"
	print(s.longestPalindrome(str2))











