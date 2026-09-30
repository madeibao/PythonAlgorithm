
from ListNode import ListNode

class Solution:
    def reverse(self, root:ListNode) -> ListNode:
        pre = None
        head = root
        while head:
            node = head.next
            head.next = pre
            pre = head
            head = node
        return pre

if __name__=="__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None

    res = Solution().reverse(a)
    while res:
        print(res.val,end=" ")
        res = res.next


