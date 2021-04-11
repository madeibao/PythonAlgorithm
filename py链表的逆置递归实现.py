
# 递归的方式来实现链表的逆置。

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def reverse(self, head):
		if head==None or head.next==None:
			return head

		temp = head.next
		res = self.reverse(temp)	

		head.next.next = head;
		head.next = None
		return res

if __name__ == '__main__':
	s = Solution()
	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)
	n5 = ListNode(4)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = None

	res = s.reverse(n2)
	while res:
		print(res.val,end="->")
		res = res.next


