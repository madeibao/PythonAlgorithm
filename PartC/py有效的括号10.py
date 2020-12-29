

class Solution():
	def legal(self,strs):

		list2 = list(strs):
		dict2 = {'(': ')','[':']','{': '}'}
		stack  = []
		for i in range(len(strs)):
			if i in dict2:
				stack.append(i)
			elif len(stack)!=None and dict2[strs[-1]]==i:
				stack.pop()
			else:
				return False
		return True


if __name__=='__main__':
	s= Solution()
	str2 ="()()"

	print(s.legal(str2))







