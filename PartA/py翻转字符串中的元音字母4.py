
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        l=len(s)
        while True:
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
	str2 = "leetcode"
	print(s.reverseVowels(str2))


#------------------------------------------------------------------------------------------------------
class Solution:
    def reverseVowels(self, s: str) -> str:
        length = len(s)
        low, high = 0, length-1
        s = list(s)
        res =['a','e','i','o','u','A','E','I','O','U']
        while low <= high: 
            while low< high and s[high] not in res:
                high-=1
            while low < high and s[low] not in res:
                low += 1
            s[low],s[high]  = s[high],s[low]
            low+=1
            high-=1
        return  "".join(s)

if __name__ "__main__":
    s =Solution()
    str2 ="leetcode"
    print(s.reverseVowels(str2))
    