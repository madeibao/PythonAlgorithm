

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head

        return temp

if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)
	n7 = ListNode(7)

	n2.next = n3	
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.swapPairs(n2)

	while res:
		print(res.val,end=' ')
		res = res.next


