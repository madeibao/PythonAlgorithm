
# 把字符串中的元音的字母来进行翻转。
# 
# leetcode 
# 翻转为
# leotcede
# -----------------------------------------------------------------------


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

	

#============================================================================

class Solution(object):
	def reverseVowels(self,strs):
		list2 = list(strs)

		i,j = 0,len(strs)-1

		while i<j:
			if list2[i] not in "aeiouAEIOU" or list2[j] not in "aeiouAEIOU":
				i+=1
				j-=1


if __name__ == "__main__":
	s = Solution()
	str2 ="leetcode"
	print(s.reverseVowels(str2))

