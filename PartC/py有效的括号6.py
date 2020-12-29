

class Solution:
    def isValid(self, s: str) -> bool:
        dic2 = {"(":")","{":"}","[":"]"}

        stack = []
        for i in range(len(s)):
            if s[i] in dic2:
                stack.append(s[i])
            elif not stack and dic2[stack[-1]]==s[i]:
                stack.pop()
            else:
                return False
        return stack==[]

if __name__=='__main__':
    s =Solution()
    str2 ="()"
    print(s.isValid(str2))