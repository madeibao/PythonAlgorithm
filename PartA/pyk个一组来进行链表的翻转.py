# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/9/26 8:43
# @File: Test


class ListNode(object):
	def __init__(self,x):
		self.val =x
		self.next = None


class Solution(object):
	def reverse(self,head,k):


		def helper(head, tail):
			pre= None
			while head!=tail:
				temp2 = head.next
				head.next= pre
				pre= head
				head=temp2
			return pre
		if not head or not head.next:
			return head
		tail = head
		for _ in range(k):
			if not tail:
				return head
			tail = tail.next

		newhead = helper(head,tail)
		head.next = self.reverse(tail, k)
		return newhead

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

    res = s.reverse(head, 2)

    while res:
    	print(res.val,end="->")
    	res = res.next

