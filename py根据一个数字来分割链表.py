

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        p1.next = None
        p2.next = None

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next


def createNode(nums):
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
	n2 = createNode([1,3,4,3,4,5,3,2,4])
	res = s.partition(n2, 3)

	while res:
		print(res.val,end="->")
		res = res.next


