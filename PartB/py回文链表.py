

from typing import List

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
    	if not head or not head.next:return True
    	stack = []

    	while head:
    		stack.append(head.val)
    		head = head.next
    	return stack==stack[::-1]

if __name__ == "__main__":
	s = Solution()
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(2)
	n2.next = n3
	n3.next = n4
	n4.next = None

	print(s.isPalindrome(n2))

