

class Solution(object):
    def legal(self,strs):
        dict2 = {'[':']', '{':'}', '(':')'}

        stack = []
        for i in strs:
            if i in dict2:
                stack.append(i)
            elif len(stack)!=0 and dict2[stack[-1]] ==i:
                stack.pop()
            else:
                return False
        return stack ==[]


if __name__ == "__main__":
    s = Solution()

    str2 = "()()"
    print(s.legal(str2))

    
