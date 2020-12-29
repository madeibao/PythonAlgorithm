

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):
	def revemoveNode(self,head):

		if not head:
			return None
		if head.next ==None:
			return head
		p2 = head

		while p2.next!=None:
			if p2.val == p2.next.val:
				p2.next = p2.next.next
			else:
				p2 = p2.next
		return head


if __name__ == "__main__":
	s= Solution()

	n2 = ListNode(1)
	n3 = ListNode(1)
	n4 = ListNode(2)
	n5 = ListNode(2)
	n6 = ListNode(3)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = None

	res = s.revemoveNode(n2)

	while res:
		print(res.val,end="->")
		res = res.next


