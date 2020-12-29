class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        last = prev.next
        while last:
            if last.val == val:
                prev.next = last.next
                last = prev.next
            else:
                prev = prev.next
                last = prev.next
        return dummy.next


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

    k = 3
    res = s.removeElements(n2, k)
    while res:
        print(res.val, end="->")
        res = res.next






