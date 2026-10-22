

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

if __name__ == "__main__":

    ListNodea = ListNode(1)
    ListNodeb = ListNode(2)
    ListNodec = ListNode(3)

    ListNodea.next = ListNodeb
    ListNodeb.next = ListNodec
    ListNodec.next = None

    solution = Solution()
    reversed_head = solution.reverseList(ListNodea)

    # 打印反转后的链表
    current = reversed_head
    while current:
        print(current.val)
        current = current.next
    
    print("反转后的链表打印完毕")