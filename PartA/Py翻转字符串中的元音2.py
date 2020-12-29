

class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        l=len(s)
        while 1:
            if left>=right:
                break
            while s[left] not in "aeiouAEIOU" and left<right:
                left+=1
            while s[right] not in "aeiouAEIOU" and right>left:
                right -= 1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return "".join(s)


if __name__ == "__main__": 
    s = Solution()
    print(s.reverseVowels("leetcode"))