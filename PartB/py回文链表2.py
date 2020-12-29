

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = []
        node = head
        while(node):
            num.append(node.val)
            node = node.next
        length = len(num)
        for i in range(length//2):
            if num[i] != num[length - 1 - i]:
                return False
        return True

if  __name__ == '__main__':
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(1)

	n2.next = n3
	n3.next = n4
	n4.next = None

	print(s.isPalindrome(n2))

