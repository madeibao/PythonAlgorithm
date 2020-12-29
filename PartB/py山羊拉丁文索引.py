


class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        def exchange(str2):
            if str2[0] in "aeiou":
                str2 = str2+"ma"
            else:
                str2 = str2[1:]+str2[0]+"ma"

        list2 = S.split(" ")

        for i in list2:
            res.append(exchange(i))


        for i in res:
            

if __name__ == "__main__":
    s  = Solution()
    str2 = "I speak Goat Latin"
    print(s.toGoatLatin(str2))

