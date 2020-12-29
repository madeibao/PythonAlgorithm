

# 在一个链表中，删除掉所有的重复的节点。
# 只要是重复的，都进行删除。

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None 


class Solution():
    def deleteDuplicates(self, head: ListNode) -> ListNode:	

    	if head==None:
    		return None

    	# 递归的写法。
    	# 第一个和后面的值是相等的。
    	if head.next and head.val==head.next.val:
    		while head.next and head.val == head.next.val:
    			head = head.next
    		return self.deleteDuplicates(head.next)
    	else:
    		head.next = self.deleteDuplicates(head.next)

    	return head


if __name__ == '__main__':
	s = Solution()

	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(2)
	n5 = ListNode(2)
	n6 = ListNode(3)
	n7 = ListNode(4)

	n2.next = n3	
	n3.next = n4
	n4.next = n5 
	n5.next = n6
	n6.next = n7
	n7.next = None

	res = s.deleteDuplicates(n2)

	while res:
		print(res.val, end=' ')
		res = res.next

