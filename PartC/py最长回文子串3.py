
# 求一个字符串的最长的回文子串
# 算法的核心思想是中心扩展算法。
#  由一个中性，来左右的扩展实现。


class Solution:
    def longestPalindrome(self, s: str) -> str:

    	def helper(s, left, right):
    		while left>=0 and right<len(s) and s[left]==s[right]:
    			left-=1
    			right+=1
    		return s[left+1:right]

    	res =s[:1]

    	for i in range(len(s)):
    		str2 = helper(s, i,i)
    		str3 = helper(s,i,i+1)
    		res = max(str2, str3, res, key = len)
    	return res

if __name__ == "__main__":
	s =Solution()
	str2 ="babad"
	print(s.longestPalindrome(str2))


