

class Solution(object):
	def getSolution(self,s):
		list2 = []

		for i in s:
			if i=='[' or i=='(' or i=='{':
				list2.append(i)
			if i==']' or i==')' or i=='{':
				if list2==[]:
					return False
				elif abs(ord(i)-ord(list2.pop(-1)))>2:
					return False
		return list2==[]


if __name__=='__main__':
	S = Solution()
	print(S.getSolution("(())"))