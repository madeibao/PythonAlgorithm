
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def combine(self,headA, headB):
		if not headA:return headB
		if not headB:return headA

		pa = headA
		pb = headB

		dummy = ListNode(-1)
		dummy.next = None
		temp = dummy


		while pa and pb:
			if pa.val<= pb.val:
				temp.next = pa
				pa = pa.next
				temp = temp.next
			else:
				temp.next = pb 
				pb = pb.next
				temp = temp.next

		if pa:
			temp.next = pa

		if pb:
			temp.next = pb 

		return dummy.next



if __name__ == "__main__":
	s =Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4) 

	n2.next = n3
	n3.next = n4
	n4.next = None

	h2 = ListNode(5)
	h3 = ListNode(6)
	h4 = ListNode(7)
	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.combine(n2,h2)

	while res:
		print(res.val,end=" ")
		res = res.next


