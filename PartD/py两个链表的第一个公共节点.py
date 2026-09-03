

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)

	h3 = ListNode(3)
	h4 = ListNode(4)

	c5 = ListNode(5)
	c6 = ListNode(6)
	c7 = ListNode(7)

	n2.next = n3
	n3.next = n4
	n4.next = c5
	c5.next = c6
	c6.next = c7

	h3.next = h4
	h4.next = c5 

	res = s.getIntersectionNode(n2, h3)
	while res:
		print(res.val,end="->")
		res = res.next

