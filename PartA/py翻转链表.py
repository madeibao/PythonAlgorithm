


class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def reverese(self,head):
		if not head:
			return None

		if not head.next:
			return head

		pre = None

		while head:
			temp2 = head.next
			head.next =pre
			pre = head
			head = temp2

		return pre

if __name__ == "__main__":
	s =Solution()
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = None

	res = s.reverese(n2)
	while res:
		print(res.val,end=" ")
		res = res.next


