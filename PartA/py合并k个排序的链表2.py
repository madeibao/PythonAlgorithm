



class ListNode():
	def __init__(self,x):
		self.value = x
		self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        import heapq
        all_vals = []
        for l in lists:
            while l:
                all_vals.append(l.val)
                l = l.next

        # 首先来进行排序
        all_vals.sort()
        dummy = ListNode(None)
        cur = dummy
        for i in all_vals:
            temp_node = ListNode(i)
            cur.next = temp_node
            cur = temp_node

        return dummy.next


if __name__ == "__main__":
	s = Solution()
	