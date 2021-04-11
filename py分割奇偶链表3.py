

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head: ListNode) -> ListNode:

		odd = head
		even = even_head = head.next
		while even.next and odd.next:
			odd.next = odd.next.next
			even.next = even.next.next

			odd = odd.next
			even = even.next
		odd.next = even_head
		return head


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)
	n5 = ListNode(4)
	n6 = ListNode(5)
	n7 = ListNode(6)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.oddEvenList(n2)
	while res:
		print(res.val,end='->')
		res = res.next




