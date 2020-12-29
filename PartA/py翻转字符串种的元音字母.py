


class Solution():
    def reverse2(self,strs):

        list2 = list(strs):
        i,j = 0, len(list2)-1

        while True:
            while i<j and list2[i] not in "aeiouAEIOU":
                i+=1
            while i<j and list2[j] not in "aeiouAEIOU":
                j-=1
            list2[i],list2[j] = list2[j],list2[i]
            i += 1
            j -= 1
        return "".join(list2)

if __name__ == "__main__":
    s = Solution()
    str2 ="leetcode"
    print(s.reverse2(str2))



