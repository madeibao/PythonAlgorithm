

class Solution(object):
	def legalBracket(self, strs):
		dic2  = {"(":")","[": "]", "{":"}",}
		stack = []	

		for i in range(len(strs)):
			if strs[i] in dic2:
				stack.append(strs[i])
			elif len(stack)!=0 and  dic2[stack[-1]] == strs[i]:
				stack.pop()
			else:
				return False
		return True 



if __name__ == "__main__":

	s = Solution()
	print(s.legalBracket("(()())"))


