
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

	n2 = ListNode(4)
	n3 = ListNode(1)

	h1 = ListNode(5)
	h2 = ListNode(0)
	h3 = ListNode(1)

	n4 = ListNode(8)
	n5 = ListNode(4)
	n6 = ListNode(5)

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = None
	
	h1.next = h2
	h2.next = h3
	h3.next = n4

	res = s.getIntersectionNode(n2, h1)

	while res:
		print(res.val, end="->")
		res= res.next

