
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseKthNode(self, head, n):

		dummy = ListNode(-1)
		dummy.next  = head

		slow = head
		fast = head

		for i in range(n):
			fast = fast.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next

		# 慢的指针来删除指针的节点的内容。
		slow.next = slow.next.next
		return dummy.next

if __name__ == "__main__":
	s =Solution()
	n2 =ListNode(2)
	n3 =ListNode(3)
	n4 =ListNode(4)
	n5 =ListNode(5)
	n6 =ListNode(6)

	n2.next =n3
	n3.next =n4
	n4.next =n5
	n5.next =n6
	n6.next =None

	res = s.reverseKthNode(n2, 3)
	while res:
		print(res.val,end="")
		res = res.next




