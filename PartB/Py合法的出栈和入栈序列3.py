



# 判断出栈和入栈的序列是否为同一个序列的值。

class Solution:
	def legal(self, pushed, poped):

		stack = []
		i,j = 0,0
		while i<len(pushed) and j<len(poped):
			stack.append(pushed[i])
			while len(stack)!=0 and j<len(poped) and stack[-1]==poped[j]:
				stack.pop()
				j +=1
			i+=1
		return stack==[]


if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,3,4,5]
	list3 = [4,5,3,2,1]

	print(s.legal(list2, list3))

