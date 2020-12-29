
# 求一个字符串的最长的回文子串。

class Solution:
    def longestPalindrome(self, s: str) -> str:

    	def spread(s,left,right):
    		while left>=0 and right<len(s) and s[left]==s[right]:
    			left-=1
    			right+=1
    		return s[left+1:right]

    	if s==s[::-1]:
    		return s

        # 默认的条件下是一个长度的值。
        # 如果所有的值都不相等的化，就是单一的一个字符的长度的值。
    	res = s[:1]

    	for i in range(len(s)):

            # 判断奇数的回文字符串结果值。
    		palindrome_odd = spread(s,i,i)

            # 判断偶数的回文字符串的结果值。
    		palindrome_even = spread(s,i,i+1)
    		res = max(palindrome_odd, palindrome_even,res, key=len)
    	return res


if __name__ == "__main__":
	s = Solution()
	str2 ="babad"
	print(s.longestPalindrome(str2))


