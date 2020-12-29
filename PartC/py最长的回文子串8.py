
# 最长的回文子串
# 最长的回文子串


class Solution(object):
    def longestPalindrome(self,strs):
        if strs==strs[::-1]:
            return strs

        def helper(s, left, right):
            while left>=0 and right<len(s):
                if s[left]==s[right]:
                    left-=1
                    right+=1
                else:
                    break
            return s[left+1:right]
        res = strs[:1]

        for i in range(len(strs)):
            temp2 = helper(strs,i,i)
            temp3 = helper(strs,i,i+1)
            res = max(res, temp2, temp3, res, key=len)
        return res

if __name__ == "__main__":
    s = Solution()
    str2 = "babad"
    print(s.longestPalindrome(str2))









