class Solution:
    def reverseVowels(self, s: str) -> str:
        list2 = list(s)

        i,j = 0,len(list2)-1
        str2 ="aeiouAEIOU"
        while i<j:
            if list2[i] in str2 and list2[j] in str2:
                list2[i],list2[j] = list2[j],list2[i]
                i+=1
                j-=1
                
            if list2[i] not in str2:
                i+=1
            if list2[j] not in str2:
                j-=1
        
        return "".join(list2)


if __name__ == "__main__":
    s = Solution()
    str2 = "hello"
    print(s.reverseVowels(str2))
	


