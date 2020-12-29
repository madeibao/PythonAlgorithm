
# 字符串能否通过删除一个或者是多个字符来变成回文的字符串


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                str_left=s[:i]+s[i+1:]
                if str_left==str_left[::-1]:
                    return True
                str_right=s[:j]+s[j+1:]
                if str_right==str_right[::-1]:
                    return True
                return False
        return True

if __name__=='__main__':
    s = Solution()
    print(s.validPalindrome("abab"))

