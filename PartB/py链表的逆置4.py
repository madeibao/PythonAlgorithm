

# 链表的逆置的操作。

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None 

class Solution():
	def reverseNode(self,head):

		if not head:
			return None

		if not head.next:
			return head
		pre = None

		while head:
			temp = head.next
			head.next = pre
			pre = head
			head = temp

		return pre

if __name__ == "__main__":
	s =Solution()
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)

	n2.next = n3	
	n3.next = n4
	n4.next = n5
	n5.next = None

	res = s.reverseNode(n2)

	while res:
		print(res.val)
		res= res.next






