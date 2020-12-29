

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None 

# 递归的解法来实现链表的逆置


class Solution(object):
	def reverse(self,head):
		if not head or not head.next:
			return head

		root = self.reverse(head.next)
		head.next.next = head
		head.next = None
		return root


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)

	n2.next = n3
	n3.next = n4
	n4.next = n5 
	n5.next = None

	res=s.reverse(n2)

	while res:
		print(res.val, end="->")
		res = res.next

