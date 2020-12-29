
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py合并两个有序链表.py
@Time    :   2020/11/27 12:12:48
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None #


class Solution(object):
    def combine(self,headA, headB):

        if not headA:
            return headB    
        if not headB:
            return headA

        p1 = headA
        p2 = headB

        temp = None

        if(p1.val<p2.val):
            temp = p1
            temp.next =self.combine(p1.next, p2)
        else:
            temp = p2
            temp.next =self.combine(p1,p2.next)
        return temp

def createListNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


if __name__ == "__main__":
    s = Solution()
    head2 = createListNode([1, 2, 3, 4])
    head3 = createListNode([2, 3, 3])

    res = s.combine(head2, head3)

    while res:
        print(res.val, end='->')
        res = res.next
