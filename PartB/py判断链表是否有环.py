

class ListNode(object):
	def __init__(self, x):
		self.val =x 
		self.next = None 


class Solution():
	def circle(self,head):

		if head==None or head.next==None:
			return False

		fast = head
		slow = head

		while fast.next and fast.next.next:
			fast = fast.next.next
			slow = slow.next
			if slow==fast:
				return True
		return False



if __name__=='__main__':
	s = Solution()


	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)

	n6 = ListNode(6)

	n7 = ListNode(7)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6

	n6.next = n7
	n7.next = n4

	print(s.circle(n2))



