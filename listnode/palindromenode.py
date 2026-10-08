
from typing import Optional
from typing import List
from ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        pa = head
        pb = head
        while pb and pb.next:
            pa = pa.next
            pb = pb.next.next

        prev = self.reversenode(pa)

        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

    def reversenode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


if __name__ == "__main__":
    s = Solution()

    pa = ListNode(1)
    pb = ListNode(2)
    pc = ListNode(1)
    pa.next = pb
    pb.next = pc
    pc.next = None

    print(s.isPalindrome(pa))
