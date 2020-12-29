
# 把一个链表的倒数的第n个节点来进行删除。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def remove(self, head, n):

        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = None

    k = 2
    res = s.remove(n1, k)
    while res:
        print(res.val, end="->")
        res = res.next



