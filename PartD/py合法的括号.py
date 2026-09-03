
# 合法的括号
# 判断是否合法的括号。


class Solution(object):
	def legal(self, strs):
		dict2 = {"(":")","{":"}","[":"]"}
		stack = []

		for i in strs:
			if i in dict2:
				stack.append(i)
			elif len(stack)!=0 and i ==dict2[stack[-1]]:
				stack.pop()
			else:
				return False
		return not stack 

if __name__ == '__main__':	
	s = Solution()
	str2 ="()[]"
	print(s.legal(str2))





