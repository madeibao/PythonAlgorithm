
# 通过递归的写法来两两的交换链表中的两个相邻的节点的内容。
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def exchangeNode(self,head):

		# 如果是只有一个节点或者是链表为空，直接的返回就可以。
		if head is None or head.next is None:
			return head

		temp = head
		headnext = temp.next

		# 关键的语句，递归的写法。
		temp2 = self.exchangeNode(headnext.next)

		temp.next = temp2
		headnext.next = temp
		return headnext

if __name__ == "__main__":
	s =Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(4)
	n5 = ListNode(9)
	n6 = ListNode(8)
	n7 = ListNode(5)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None	

	res = s.exchangeNode(n2)

	while res:
		print(res.val,end=' ')
		res = res.next
