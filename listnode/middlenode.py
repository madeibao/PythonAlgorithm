
from ListNode import ListNode

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        ha = head
        hb = head

        while hb and hb.next:
            ha = ha.next
            hb = hb.next.next
        return ha


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = None

    s = Solution()
    node = s.middleNode(head)
    print(node.val)