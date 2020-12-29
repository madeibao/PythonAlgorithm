

class ListNode(object):
	def __init__(self,x):
		self.val = x 
		self.next = None

class ListNode(object):
	def printListNode(self, head):

		stack = []
		while head:
			stack.append(head.val)
			head = head.next

		return stack[::-1]

if __name__ == '__main__':
	s =Solution()
	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n2.next = n3
	n3.next = n4
	n4.next = None

	print(s.printListNode(n2))


