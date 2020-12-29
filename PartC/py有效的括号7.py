


# 判断是否为合法的匹配括号算法。

class Solution:
    def isValid(self, s: str) -> bool:
        dic2 = {"(":")","{":"}","[":"]"}

        stack = []

       	for i in range(len(s)):
       		if s[i] in dic2:
       			stack.append(s[i])
       		else:
       			if len(stack)!=0 and dic2[stack[-1]]==s[i]:
       				stack.pop()

       	return stack ==[]


if __name__ == "__main__":
	s =Solution()
	str2 ="()()[]"
	print(s.isValid(str2))

