# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2

        # 设置进位。

        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while p1 or p2:
            x = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            val, carry = x % 10, x // 10
            cur.next = ListNode(val)
            cur = cur.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next

            
        # 如果进位不是0的条件下，仍然要添加进位。
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next


if __name__ == "__main__":
	s =Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)

	n2.next = n3
	n3.next = n4
	n4.next = None

	h2 = ListNode(2)
	h3 = ListNode(3)
	h4 = ListNode(4)
	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.addTwoNumbers(n2,h2)

	while res:
		print(res.val,end="->")
		res =res.next

