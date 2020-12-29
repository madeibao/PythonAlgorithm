
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
	def exchange(self,head):
		if head is None:
			return None

		if head.next is None:
			return head 
		temp= head.next
		temp2 =exchange(temp.next)

		head.next = temp2
		temp.next = head

		return temp 


if __name__ == "__main__":
	s =Solution()

	head = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(3)
	n5 = ListNode(4)
	n6 = ListNode(4)
	n7 = ListNode(5)

	head.next = n2
	n2.next =n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.exchange(head)

	while res:
		print(res.val,end="->")
		res =res.next


