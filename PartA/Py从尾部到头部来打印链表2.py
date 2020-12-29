

from typing import List

class ListNode(object):
	def __init__(self,x):
		self.val = x 
		self.next = None 


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]  # 或者 reverse(res)


if __name__ == "__main__":
	s = Solution()
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)

	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = None

	print(s.reversePrint(n2))

	
