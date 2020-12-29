


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True

if __name__ == "__main__":
    s =Solution()
    print(s.validPalindrome("aba"))

#-----------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------


class Solution(object):
    def validPalindrome(self, s):
        isPalindrome = lambda x:x==x[::-1]

        left, right = 0, len(s)-1

        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
            else:

                # 相当于Java语言的 isPalindrome(s, left+1， right) or isPalindrome(s, left, right-1)

                # python的字符串的截取包括开始，不包括结尾。
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
        return True 


