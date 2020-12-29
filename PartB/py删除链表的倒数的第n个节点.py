# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/9/26 8:43
# @File: Test

# 删除链表的倒数的第 n 个节点的值。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
            slow = slow.next
            fast = fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

def createListNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


if __name__ == '__main__':

    temp = createListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    n = 2
    s = Solution()
    res = s.removeNthFromEnd(temp, n)

    while res:
        print(res.val,end="->")
        res =res.next














