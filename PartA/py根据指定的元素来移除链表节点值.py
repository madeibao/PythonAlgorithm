

# 删除链表中的与给定值相同的节点的值。
# 删除链表的指定的节点的值。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def remove(self, head, val):

        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy.next
        prev = dummy

        while cur != None:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(6)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n7 = ListNode(5)
    n8 = ListNode(6)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = None

    k = 6
    res = s.remove(n2, k)
    while res:
        print(res.val)
        res = res.next
