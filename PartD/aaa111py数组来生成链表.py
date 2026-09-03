

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


# 数组来生成一个链表。
def createNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def printNode(head):
	if head is None:
		return
	cur = head
	while cur:
		print(cur.val,end="->")
		cur = cur.next
	print('null')



if __name__ == "__main__":
	nums = [1,2,3,4]
	res = createNode(nums)
	printNode(res)

