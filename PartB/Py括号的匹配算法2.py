
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []                         #第一个栈用来记录所有(的index
        star_stack = []                    #第二个栈用来记录所有*的index
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if not stack and not star_stack:
                    return False                        #如果直接读到)，直接return False
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()                    #先用(来消)，再用*来消)

  
        while stack and star_stack:
            if stack.pop() > star_stack.pop():          #在所有)都处理了之后，只需要考虑(和*的index，此时的*全部当作)来考虑，比较index即可
                return False
        return not stack                   #判断是否有多余的(


if __name__ == "__main__": 
	s = Solution()
	str2 =  "(*)"
	print(s.checkValidString(str2))

