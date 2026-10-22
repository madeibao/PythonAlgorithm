
from ListNode import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        # 找到中间节点，然后断开链表为两个部分
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None

        # 将 l2 部分反转
        l2 = self.reverseList(l2)

        # 然后交替合并两部分
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
    
    def middleNode(self, head: ListNode) -> ListNode:
        ha = head
        hb = head

        while hb and hb.next:
            ha = ha.next
            hb = hb.next.next
        return ha

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = None

    sol = Solution()
    sol.reorderList(a)
    while a:
        print(a.val)
        a = a.next

