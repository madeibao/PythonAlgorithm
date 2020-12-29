


class Solution(object):
	def legalBracket(self,strs):
		if not strs:
			return True
		stack= []
		dict2 = {"{":"}", "[":"]", "(":")"}

		for i in range(len(strs)):
			if strs[i] in dict2:
				stack.append(strs[i])
			elif len(stack)!=0 and dict2[stack[-1]]==strs[i]:
				stack.pop()
			else:
				return False
		return stack==[]


if __name__ == "__main__":
	s = Solution()
	str2= "()()"
	print(s.legalBracket(str2))

