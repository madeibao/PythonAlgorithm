
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self , head ):
        # write code here
        # 同时指向头节点的值。
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 后面保持速度一致的条件下。
            if slow == fast:
                res = head
                while res!=slow:
                    res = res.next
                    slow = slow.next
                return res
        return None



if __name__ == "__main__":
	s =Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)
	n6 = ListNode(6)



	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6 
	n6.next = n3

	res = s.detectCycle(n2)

	print(res.val)

