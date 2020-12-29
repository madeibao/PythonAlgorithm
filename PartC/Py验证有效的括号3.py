

class Solution(object):
	def validbracket(self,strs):
		stack = []
		star_stack = []

		for i in range(len(strs)):
			if strs[i]=='(':
				stack.append(strs[i])
			elif strs[i]== '*':
				star_stack.append(strs[i])

			else:
				if not stack and not star_stack:
					return False
				if stack:	
					stack.pop()
				elif star_stack:
					star_stack.pop()


		while stack and star_stack:
			if stack.pop()>star_stack.pop():
				return False 
		return not stack



if __name__ == '__main__':
	s = Solution()
	print(s.validbracket("(*)"))

