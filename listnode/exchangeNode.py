# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 11:12
# @File: exchangeNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        if head.next is None:
            return head

        nodea = head.next
        nodeb = self.swapPairs(nodea.next)
        head.next = nodeb
        nodea.next = head
        return nodea

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = None

    s = Solution()
    node = s.swapPairs(head)
    while node:
        print(node.val)
        node = node.next
