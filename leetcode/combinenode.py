

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def combine(self, nodea:ListNode, nodeb:ListNode) -> ListNode:
		if nodea is None:
			return nodeb
		if nodeb is None:
			return nodea
		res = None

		dummy = ListNode(-1)
		res = dummy

		while nodea and nodeb:
			if nodea.val < nodeb.val:
				res.next = nodea
				nodea = nodea.next
			else:
				res.next = nodeb
				nodeb = nodeb.next
			res = res.next

		if nodea:
			res.next = nodea
		
		if nodeb:
			res.next = nodeb

		return dummy.next

if __name__ == "__main__":
	nodea = ListNode(1)
	nodea.next = ListNode(3)
	nodea.next.next = ListNode(5)

	nodeb = ListNode(2)
	nodeb.next = ListNode(4)
	nodeb.next.next = ListNode(6)

	solution = Solution()
	result = solution.combine(nodea, nodeb)

	while result:
		print(result.val, end=" -> ")
		result = result.next



