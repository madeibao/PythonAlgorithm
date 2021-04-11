

class Solution(object):
	def stackOrder(self,pushed, popped):
		stack = []

		j = 0
		for x in pushed:
			stack.append(x)
			if len(stack)>0 and j<len(popped) and stack[-1] == popped[j]:
				j+=1
				stack.pop()
		return stack==[] 


if __name__ == "__main__":
	s = Solution()
	pushed = [1,2,3,4,5,6]
	poped = [1,2,3,4,5,6]

	print(s.stackOrder(pushed, poped))