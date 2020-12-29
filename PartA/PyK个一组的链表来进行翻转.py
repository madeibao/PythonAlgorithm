# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/9/26 8:43
# @File: Test


# k个一组来进行链表的翻转操作。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        tail = head
        for i in range(k):
            # 剩余数量小于k的话，则不需要反转
            if not tail:
                return head
            tail = tail.next

        # 反转前k个元素，将返回的头结点记为newHead
        newHead = self.reverse(head, tail)
        # 将head.next 赋为 递归上一步反转得到的newHead
        head.next = self.reverseKGroup(tail, k)
        return newHead

    # 将一个范围内你的数据来进行翻转。
    # 翻转为左闭又开区间，所以本轮操作的尾结点其实就是下一轮操作的头结点
    # 包含左面，但是不包含右面的内容。
    
    def reverse(self, head, tail):
        pre = None
        while head != tail:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre


if __name__ == "__main__":
    s = Solution()

    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    k = 2
    res = s.reverseKGroup(head, k)
    while res:
        print(res.val, end="->")
        res = res.next

