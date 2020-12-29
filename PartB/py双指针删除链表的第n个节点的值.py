

# 删除链表中的倒数的第n个节点的值。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #时间复杂为O(n),空间复杂为O(1)
        fast = ListNode(0)
        slow = ListNode(0)
        fast.next = head
        slow.next = head
        dummy = slow
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            dummy = dummy.next
        dummy.next = dummy.next.next
        return slow.next


if __name__ == "__main__":
    s = Solution()

    nhead = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    nhead.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    res = s.removeNthFromEnd(nhead, 2)

    while res:
        print(res.val,end="->")
        res = res.next

