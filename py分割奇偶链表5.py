


class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def split(self,head, x):

		prea = dummy1 = ListNode(0)
		preb = dummy2 = ListNode(0)

		prea.next = None
		preb.next = None

		while head:
			if head.val <x:
				prea.next = head
				prea = prea.next
			else:
				preb.next = head
				preb = preb.next

			head = head.next


		# 把两个链表的链接起来作为最终的结果值
		prea.next = dummy2.next
		preb.next = None
		return dummy1.next


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(4) 
	n4 = ListNode(3)
	n5 = ListNode(2)
	n6 = ListNode(5)
	n7 = ListNode(2)

	n2.next=n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7	
	n7.next = None

	res = s.split(n2,3)

	while res:
		print(res.val, end="->")
		res = res.next
