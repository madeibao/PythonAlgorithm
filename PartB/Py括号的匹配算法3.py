


# (*)
# 一个括号的匹配中，*号可以是（
# *号也可以是）
# *号也可以是 ""

class Solution():
	def legal(self,strs):

		stack = []
		stack2 = []

		for i in range(len(strs)):
			if strs[i]=="(":
				stack.append(i)
			elif strs[i]=="*":
				stack2.append(i)
			else:
				if not stack and not stack2:
					return False
				elif not stack:
					stack.pop()
				elif not stack2:
					stack2.pop()

		while stack2 and stack:
			if stack.pop()>stack2.pop():
				return False

		return not stack

if __name__ == "__main__":
	s = Solution()
	str2 = "(*)"
	print(s.legal(str2))


#=------------------------------------------------------------------------------------------------
# 完整的括号的匹配。
# (){}[]


class Solution:
    def isValid(self, s: str) -> bool:
        dic2 = {"(":")","{":"}","[":"]"}

        stack = []
        for i in range(len(s)):
            if s[i] in dic2:
                stack.append(s[i])
            elif len(stack)!=0 and dic2[stack[-1]]==s[i]:
                stack.pop()
            else:
                return False
        return stack==[]


if __name__ == "__main__":
    s = Solution()
    str2 = "()"
    print(s.isValid(str2))
