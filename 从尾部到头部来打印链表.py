


# 剑指offer 
from typing import List, Tuple 

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def reversePrint(self, head: ListNode) -> List[int]:
		stack = []
		while head:
			stack.append(head.val)
			head = head.next

		res = []
		while stack:
			res.append(stack.pop())
		return res 


if __name__ == '__main__':

	head = ListNode(1)
	h2 = ListNode(2) 
	h3 = ListNode(3)
	h4 = ListNode(4)

	head.next = h2
	h2.next = h3
	h3.next = h4 
	h4.next = None

	s = Solution()
	res = s.reversePrint(head)
	print(res)


