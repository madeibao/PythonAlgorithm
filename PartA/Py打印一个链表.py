


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__=='__main__': 
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4) 

	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = None

	while n1!=None:
		print(n1.val)
		n1 = n1.next

