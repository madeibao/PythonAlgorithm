
'''
class Solution(object):
	def validBracket(self,strs):
		dict2 = {'[':']', '{':'}', '(':')',}
		stack = []

		for i in range(len(strs)):
			if strs[i] in dict2:
				stack.append(strs[i])
			elif len(stack)!=0 and dict2[stack[-1]]==strs[i]:
				stack.pop()
			else:
				return False
		return stack==[]

if __name__=='__main__':
	s = Solution()
	str2 = "(){}"
	print(s.validBracket(str2))
'''



class Solution(object):
	def validBracket(self, strs):
		dict2 = {'[':']', '{':'}', '(':')'}

		stack = []

		for i in range(len(strs)):
			if strs[i] in dict2:
				stack.append(strs[i])
			elif len(stack)!=0 and dict2[strs[i]]==strs[i]:
				stack.pop()
			else:
				return False
		return True

if __name__ == '__main__':
	s =Solution()

	print(s.validBracket("()()()()()()()()()"))