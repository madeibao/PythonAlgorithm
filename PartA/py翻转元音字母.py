


class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, s.length()-1

        while i<j:
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                temp =s[i]
                s[i]=s[j]
                s[j]=temp

            i+=1
            j-=1
        return s

if __name__ == "__main__":
    s = Solution()
    str2 =leetcode"
    print(s.reverseVowels(str2))
    


