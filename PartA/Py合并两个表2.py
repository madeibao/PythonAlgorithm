
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next =None

# V 1.0，能提交
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
    
        listMerge = None
        if l1.val < l2.val:
            listMerge = l1
            listMerge.next = self.mergeTwoLists(l1.next,l2)
        else:
            listMerge = l2
            listMerge.next = self.mergeTwoLists(l2.next,l1)
        return listMerge


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    h1 = ListNode(2)
    h2 = ListNode(3)
    h3 = ListNode(4)
    h1.next= h2
    h2.next= h3
    h3.next= None
    s = Solution()
    res = s.mergeTwoLists(n1, h1)
    while res:
        print(res.val, end="->")
        res = res.next

