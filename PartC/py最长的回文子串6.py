

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

