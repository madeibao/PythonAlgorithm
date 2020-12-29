
# 合并K个有序的链表来归并成一个单一的排序链表。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
import heapq
from heapq import heappop

class Solution(object):
    def mergeKLists(self, lists:List[ListNode]):

    	# 通过建立一个堆来完成 操作。
        import heapq
        head = point = ListNode(0)
        # 首先声明的是头节点的值。
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next

        while heap:
            val = heappop(heap)
            point.next = ListNode(val)
            point = point.next
        point.next = None
        return head.next


if __name__ == "__main__": 	
	s  = Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)

	n2.next = n3
	n3.next = n4
	n4.next = None



	h2 = ListNode(3)
	h3 = ListNode(4)
	h4 = ListNode(8)

	h2.next = h3
	h3.next = h4
	h4.next = None

	res= []

	res.append(n2)
	res.append(h2)

	res = s.mergeKLists(res)

	while res:
		print(res.val,end=" ")
		res = res.next

