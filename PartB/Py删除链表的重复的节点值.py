


class ListNode():
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution():
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		temp = head

		if temp ==None:
			return None

		while temp!=None and temp.next!=None:
			if temp.val == temp.next.val:
				temp.next = temp.next.next
			else:
				temp = temp.next 
		return head



if __name__ == "__main__":
	s = Solution()
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(2)
	n4 = ListNode(3)

	n1.next = n2
	n2.next = n3 
	n3.next = n4
	n4.next = None

	res = s.deleteDuplicates(n1)

	while res:
		print(res.val, end=' ')
		res = res.next

