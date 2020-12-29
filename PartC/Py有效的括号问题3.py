


class Solution(object):
	def validBracket(self,strs):

		stack = []
		star_stack = []

		for i in strs:
			if i=='(':
				stack.append(i)
			if i=='*':
				star_stack.append(i)
			else:
				if not star_stack and not stack:
					return False
				if stack:
					stack.pop()
				elif star_stack:
					star_stack.pop()

		while star_stack and stack:
			if stack.pop()>star_stack.pop()
				return False
		return stack==[]


if __name__ == '__main__':
	s = Solution()
	strs = "(*)"
	print(s.validBracket(strs))


