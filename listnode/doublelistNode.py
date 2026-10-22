

from ListNode import ListNode
from typing import Optional

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        rev = self.reverseListNode(head)
        carry = 0
        dummy = ListNode(0)
        tail = dummy
        curr = rev
        while curr is not None or carry > 0:
            val = curr.val if curr else 0
            total = 2 * val + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            # 如果curr不为空，则移动到下一个节点
            if curr:
                curr = curr.next
        return self.reverseListNode(dummy.next) # 注意！返回dummy.next，不要dummy

    def reverseListNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


if __name__ == '__main__':
    s = Solution()
    head = ListNode(9)
    head.next = ListNode(9)
    head.next.next = ListNode(9)
    

    res = s.doubleIt(head)
    while res:
        print(res.val)
        res = res.next
