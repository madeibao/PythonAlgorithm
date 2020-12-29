

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
	def reverseNode(self,head):
		pre = None

		while head:
			temp = head.next
			head.next = pre 
			pre = head
			head = temp

		return pre

if __name__ == "__main__":
	s =Solution()

	a2 = ListNode(2)
	a3 = ListNode(3)
	a4 = ListNode(4)

	a2.next = a3
	a3.next = a4
	a4.next = a5

	res = s.reverseNode(a2)
	while res:
		print(res.val,end=" ")
		res = res.next




