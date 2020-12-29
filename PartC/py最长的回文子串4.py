

# 最长的回文子串的值。


class Solution():
    def maxLength(self, strs):

        if strs == strs[::-1]:
            return strs

        def fun2(strs, i, j):
            while i >= 0 and j < len(strs) and strs[i] == strs[j]:
                i -= 1
                j += 1
            return strs[i + 1:j]

        res = strs[:1]
        for i in range(len(strs)):
            palindrome2 = fun2(strs, i, i)
            palindrome3 = fun2(strs, i, i + 1)
            res = max(palindrome2, palindrome3, res, key=len)
        return res


if __name__ == '__main__':
    s = Solution()
    str2 = "babad"
    print(s.maxLength(str2))



#_----------------------------------------------------------------

class Solution(object):
    def maxLength(self, strs):

        if strs == strs[::-1]:
            return strs

        def palindrome(s, i, j):
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            return s[i+1:j]

        res = strs[:1]
        for i in range(len(strs)):
            temp2 = palindrome(strs, i, i)
            temp3 = palindrome(strs, i, i + 1)

            res = max(temp2, temp3, res, key=len)
        return res


if __name__ == "__main__":
    s = Solution()
    str2 = "babad"
    print(s.maxLength(str2))









