


class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def reverse(self,head):
		if head==None or head.next == None:
			return head

		pre = None
		while head:
			temp = head.next
			head.next = pre
			pre = head
			head =temp
		return pre


if __name__ == "__main__":
	s = Solution()
	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n2.next = n3
	n3.next = n4
	n4.next = None

	res = s.reverse(n2)
	while res:
		print(res.val ,end=' ')
		res = res.next

