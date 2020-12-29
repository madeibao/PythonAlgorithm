

class ListNode(object):
	def __init__(self,x):
		self.val =x 
		self.next = None 


class Solution(object):
	def combine(self,headA, headB):
		if headA==None:
			return headB	
		if headB==None:
			return headA

		temp =ListNode(-1)
		dummy = temp

		a = headA
		b = headB
		while a!=None and b!=None:
			if a.val<b.val:
				dummy.next = a
				a =a.next
			else:
				dummy.next = b 
				b =b.next
			dummy = dummy.next

		if a!=None:
			dummy.next =a

		if b!=None:
			dummy.next =b
		return temp.next

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


