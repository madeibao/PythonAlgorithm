


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=collections.Counter(s)
        res=0
        #看有没有出现奇数
        odd=0
        for i in d:
            if d[i]%2==0:
                res+=d[i]
            elif d[i]%2==1:
                odd=1
                res+=d[i]-1
        return res+1 if odd else res


if __name__=='__main__':
	s= Solution()
	str2 = "abccccdd"
	print(s.longestPalindrome(str2))

	
