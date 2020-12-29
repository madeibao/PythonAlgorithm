

class Solution():
    def maxPalindrome(self,strs):

        def helper(strs,i,j):
            # 中心扩展的算法。
            while i>=0 and j<len(strs) and strs[i]==strs[j]:
                i -=1
                j +=1
            return s[i+1:j]
    
        # 如果本身就是一个回文字符串，那么就直接的返回本身的内容就行。
        if strs==strs[::-1]:
            return strs

        strs = strs[:1]

        for i in range(len(strs)):
            palindrome2 = helper(strs,i,i)
            palindrome3 = helper(strs,i,i+1)
            strs = max(palindrome2,palindrome3,strs,key = len)
        return strs

if __name__ == "__main__":
    s =Solution()
    str2 = "leetcode"
    print(s.maxPalindrome(str2))



                