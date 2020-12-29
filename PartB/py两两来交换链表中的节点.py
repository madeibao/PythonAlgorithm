
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def reverse(self, head):

		if not head or not head.next:
			return head

		temp2 = head.next
		temp3 = self.reverse(temp2.next)
		head.next = temp3
		temp2.next = temp3
		return temp2 

if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = None

	res = s.reverse(n2)

	while res:
		print(res.val, end="->")
		res = res.next 

