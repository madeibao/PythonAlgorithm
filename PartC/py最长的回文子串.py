

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s==s[::-1]:return s
        def helper(strs, i, j):
            while i>=0 and j<len(strs) and strs[i]==strs[j]:
                    i-=1
                    j+=1
            return s[i+1:j]

        res = s[:1]
        for i in range(len(s)):
            temp = helper(s, i, i)
            temp2 = helper(s, i, i+1)
            res = max(temp, temp2, res, key = len)
        return res


if __name__ == "__main__":
    s = Solution()
    str2 = "babad"
    print(s.longestPalindrome(str2))

