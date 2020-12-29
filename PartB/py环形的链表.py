

# 判断一个链表是否有环。
# 
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        set2 = set()
        node = head
        while node:
            if node in set2:
                return node
            set2.add(node)
            node = node.next
        return None 

if __name__ == "__main__":
    s = Solution()

    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(0)
    n5 = ListNode(-4)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3


    print(s.detectCycle(n2).val)