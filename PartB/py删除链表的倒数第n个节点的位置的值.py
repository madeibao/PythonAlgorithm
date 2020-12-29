


# 删除链表中的倒数的第k个节点的值。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def kthNodes(self, head, n):


        # 首先设置一个虚拟的节点来实现作为头节点使用。

        
        slow = ListNode(-1)
        fast = ListNode(-1)

        slow.next = head
        fast.next = head

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


if __name__ == "__main__":
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    k = 2
    res = s.kthNodes(n1, k)

    while res:
        print(res.val, end="->")
        res = res.next





