

class ListNode(object):
	def __init__(self,x):
		self.val = x 
		self.next = None

class Solution(object):
	def insertSort(self,head):
		if not head:return head
		dummy = ListNode(-1)

		p1 = head

		while p1:
			temp = p1.next
			p2 = dummy

			while p2.next and p2.next.val<p1.val:
				p2 = p2.next

			p1.next = p2.next
			p2.next = p1
			p1 = temp

		return dummy.next


if __name__ == "__main__":
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(4)
    n8 = ListNode(7)


    n2.next = n3    
    n3.next = n4
    n4.next = n5 
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = None
    s =Solution()
    res = s.insertSort(n2)

    while res:
    	print(res.val,end=" ")
    	res  = res.next

