


# 合并两个有序的链表结构


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

		dummy =ListNode(-1)
		temp = dummy

		a = headA
		b = headB
		while a and b:
			if a.val<b.val:
				temp.next = a
				a =a.next
			else:
				temp.next = b 
				b =b.next
			temp= temp.next


		if a!=None:
			temp.next =a

		if b!=None:
			temp.next =b
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


