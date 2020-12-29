

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None 


'''
class Solution(object):
	def combine(self,headA,headB):

		if not headA:
			return headB	

		if not headB:
			return headA

		dummy = ListNode(-1)
		dummy.next = None
		temp = dummy

		while headA and headB:
			if headA.val<=headB.val:
				temp.next = headA
				headA = headA.next
				temp = temp.next
			else:
				temp.next = headB
				headB = headB.next
				temp = temp.next

		if headA:
			temp.next = headA

		if headB:
			temp.next = headB

		return dummy.next


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n2.next = n3	
	n3.next = n4
	n4.next = None

	h2 = ListNode(3)
	h3 = ListNode(4)
	h4 = ListNode(5)	

	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.combine(n2, h2)

	while res:
		print(res.val, end="->")
		res = res.next
'''
# 下面是递归的写法来实现链表的归并。

'''

class Solution(object):
	def combine(self,headA, headB):

		# 递归的结束的条件值。
		if not headA:
			return headB

		if not headB:
			return headA

		temp = None

		if headA.val<=headB.val:
			temp = headA
			temp.next = self.combine(headA.next, headB)
			# temp = temp.next
		else:
			temp = headB
			temp.next = self.combine(headA, headB.next)
			# temp = temp.next	
		return temp

if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n2.next = n3	
	n3.next = n4
	n4.next = None

	h2 = ListNode(3)
	h3 = ListNode(4)
	h4 = ListNode(5)	

	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.combine(n2, h2)

	while res:
		print(res.val, end="->")
		res = res.next


'''


class Solution(object):
	def combine(self, headA, headB):
		if not headA:
			return headB	
		if not headB:
			return headA

		dummy = ListNode(-1)
		dummy.next = None

		temp = dummy
		while headA and headB:
			if headA.val<=headB.val:
				temp. next = headA
				headA = headA.next
				temp = temp.next
			else:
				temp.next = headB
				headB = headB.next
				temp = temp. next

		if headA:
			temp.next = headA

		if headB:
			temp.next = headB

		return dummy.next


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n2.next = n3	
	n3.next = n4
	n4.next = None

	h2 = ListNode(3)
	h3 = ListNode(4)
	h4 = ListNode(5)	

	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.combine(n2, h2)

	while res:
		print(res.val, end="->")
		res = res.next
