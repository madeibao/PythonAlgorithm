
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   py分割奇偶链表.py
@Time    :   2021/01/01 10:42:08
@Author  :   mayuan
@Version :   1.0
@Contact :   2901429479@qq.com
@License :   (C)Copyright 2020-2021
@Desc    :   None
"""

# 1->2->3->4->5
# 1->3->5->2->4->

from typing import List, Tuple

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1 = head
        p2 = p3 = head.next
        while p1.next and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = p3
        return head
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
解题思路
拿到题目之后，第一时间想到的是把链表分成两条：一条奇数，一条偶数，这应该算是最朴素的想法了然后把它们连起来
所以我做了如下操作：
第一步：头节点肯定是奇数节点，这毋庸置疑。所以odd = head，把头节点拿出来当奇数链表的头节点
第二步：头节点的下一个节点肯定是偶数节点了，所以even = head.next，把 head.next拿出来当偶数链表的头节点，这里要注意了，一定要把偶数链表的头节点单独拿出来，这里我后面详细说
第三步：找出关系式，奇数链表的下下个节点才会是奇数节点，同样偶数节点的下下个节点才会是偶数节点

odd.next = odd.next.next
even.next = even.next.next
PS:之前做链表题目的时候，.next我经常搞混，但做得多了，我总结了一条经验
‘=’左边的.next一般指的是该节点中存的next（链表节点包括两个部分组成，一个是val，一个是next用于指向下一个部分的），而右边的.next一般来讲是指的指向的某个具体节点
第四步：找循环终止的条件，什么时候我们可以把所有的节点全部取完？
当odd.next == None or even.next == None时，代表奇数或者偶数已经全部取完了，剩下的一个会根据它是奇数还是偶数填充到对应链表中
所以循环条件为


while odd.next and even.next:
odd和even链表的头节点进一位

odd,even = odd.next,even.next
第五步：我第二步说的，为什么要把头节点拿出来，因为奇数链表的尾节点要跟偶数链表的头节点相连，从而形成完整的链表

odd.next = even_head

作者：zbzzbz
链接：https://leetcode-cn.com/problems/odd-even-linked-list/solution/zui-po-su-de-xiang-fa-dai-ma-zhu-shi-fei-chang-xia/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

# 分割奇偶链表
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd,even = odd.next,even.next
        odd.next = even_head
        return head


if __name__ == "__main__":
    s = Solution()

    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)

    n2.next = n3 
    n3.next = n4 
    n4.next = n5
    n5.next = n6
    n6.next = None

    res = s.oddEvenList(n2)

    while res:
        print(res.val,end="->")
        res =res.next
    
