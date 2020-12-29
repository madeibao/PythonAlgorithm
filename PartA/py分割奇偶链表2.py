
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


# 生成一个链表。
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
	nums = [1,2,3,3,4,5,6,7]

	temp = createListNode(nums)
	res = s.oddEvenList(temp)
	while res:
		print(res.val,end=" ")
		res = res.next





