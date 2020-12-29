


#leetcode 1047


class Solution(object):
	def des(self,S):

		stack = []
		for e in S:
			if stack and stack[-1]==e:
				stack.pop()
			else:
				stack.append(e)

		return "".join(stack)


if __name__ == "__main__":
	s = Solution()
	str2 = "abbaca"
	print(s.des(str2))

