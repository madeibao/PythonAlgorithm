
# leetcode 86
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

    	# 创建了两个虚拟的节点值。
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next


if __name__ == "__main__":
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(4) 
	n4 = ListNode(3)
	n5 = ListNode(2)
	n6 = ListNode(5)
	n7 = ListNode(2)

	n2.next=n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7	
	n7.next = None

	res = s.partition(n2,3)

	while res:
		print(res.val, end="->")
		res = res.next
