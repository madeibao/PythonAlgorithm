# leetcode 86
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            cur = head
            head = head.next  # 先移动head，把cur摘出来
            cur.next = None   # 切断旧指针，消除环隐患

            if cur.val < x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next

        p1.next = dummy2.next
        return dummy1.next


if __name__ == "__main__":
    s = Solution()

    n2 = ListNode(1)
    n3 = ListNode(4)
    n4 = ListNode(3)
    n5 = ListNode(2)
    n6 = ListNode(5)
    n7 = ListNode(2)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    res = s.partition(n2, 3)

    while res:
        print(res.val, end="->")
        res = res.next
