



class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
    def reverseNodes(self, head: ListNode) -> ListNode:

    	if head is None or head.next is None:
    		return head


    	pre = None
    	while head:
    		temp = head.next
    		head.next = pre
    		pre = head
    		head = temp

    	return pre	


if __name__ == "__main__":
	s = Solution()
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

	res= s.reverseNodes(n2)
	while res:
		print(res.val,end=" ")
		res = res.next

