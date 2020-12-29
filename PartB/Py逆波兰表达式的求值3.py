
from typing import List


class Solution(object):
	def evalRPN(self,tokens:List[str])->int:

		stack = []
		for i in range(len(tokens)):
			if tokens[i] not in ["+", "-","*", "/"]:
				stack.append(int(tokens[i]))
			else:
				a = stack.pop()
				b = stack.pop()
				if tokens[i]=="/":
					num = b//a
					if num<0 and b%a!=0:
						stack.append(num+1)
					else:
						stack.append(num)
				if tokens[i]=="+":
					stack.append(b+a)
				if tokens[i]=="-":
					stack.append(b-a)
				if tokens[i]=="*":
					stack.append(b*a)
		return stack[-1]

if __name__ == "__main__":
	s = Solution()
	list2 = ["2", "1", "+", "3", "*"]
	print(s.evalRPN(list2))
