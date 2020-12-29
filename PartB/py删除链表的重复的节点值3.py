


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = ListNode(0)
        tmp.next = head
        cur_pre = tmp
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                cur_pre.next = cur
            else:
                cur = cur.next
                cur_pre = cur_pre.next
        return tmp.next




if __name__  == "__main__":

	s =Solution()

	head = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(3)
	n5 = ListNode(4)
	n6 = ListNode(4)
	n7 = ListNode(5)

	head.next = n2
	n2.next =n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.deleteDuplicates(head)

	while res:
		print(res.val,end="->")
		res =res.next
















