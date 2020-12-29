


# 通过栈来判断字符串是否为合法的内容。


class Solution(object):

	def getSolution(self,s):

		dict2 ={'[':']','{':'}','(':')'}
		stack =[]
		list2 = list(s)

		for  item in list2:
			if item in dict2.keys():
				stack.append(item)

			elif item in dict.values():
				if len(stack)==0 or dict2.get(stack[-1])!=item:
					return False
				else:
					stack.pop()

		
		if len(stack)==0:
			return True
		else:
			return False

if __name__ == "__main__": 
	s= Solution()
	print(s.getSolution("(){}"))






