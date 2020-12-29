

# 判断括号是否匹配。


class Solution():
	def validBracket(self,str):

		dict2 = {'[':']', '(':')','{':'}'}
		stack = []

		for i in list(str):
			if i in dict2:
				stack.append(i)
			else if len(stack)!= 0 and dict2[stack[-1]]==i:
				stack.pop()
			else:
				return False

		return True

if __name__=='__main__':
	s =Solution()
	str2 = "(){}"
	print(s.validBracket(str2))

