
from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return None
        if not head.next:
            return None

        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    node = s.removeNthFromEnd(head, 2)
    while node:
        print(node.val)
        node = node.next




