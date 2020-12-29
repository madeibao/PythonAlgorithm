
class ListNode(object):
    def __init__(self,x):
        self.val = x 
        self.next = None

def insertionSortList(head: ListNode) -> ListNode:
    if not head:
        return head
    dummy = ListNode(-1)

    # p1 指向节点 v
    p1 = head
    while p1:
        t = p1.next
        # p2 始终每次的都指向第一个虚拟的节点值。
        p2 = dummy
        while p2.next and p2.next.val < p1.val:
            p2 = p2.next
        # p2.next 就是第一个不小于 v 的节点 u

        # 将 v 插入到 u 之前
        p1.next = p2.next
        p2.next = p1
        p1 = t

    return dummy.next

if __name__ == "__main__":
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(4)
    n8 = ListNode(7)


    n2.next = n3    
    n3.next = n4
    n4.next = n5 
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = None

    res = insertionSortList(n2)
    while res:
        print(res.val, end=' ')
        res = res.next

