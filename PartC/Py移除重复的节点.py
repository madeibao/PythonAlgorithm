

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        set2 = set()

        set2.add(head.val)

        res= head
        while res.next:
        	if res.next.val in set2:
        		res.next = res.next.next
        	else:
        		set2.add(res.next.val)
        		res = res.next

        return head
        

if __name__ == "__main__":
	s = Solution()
	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(3)
	n5 = ListNode(3)
	n6 = ListNode(2)
	n7 = ListNode(1)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.removeDuplicateNodes(n2)

	while res:
		print(res.val,end=" ")
		res = res.next



