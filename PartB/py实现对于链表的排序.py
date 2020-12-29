

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def sort(self,head):
        list2 = []
        ptr = head

        while ptr:
            list2.append(ptr.val)
            ptr =ptr.next

        ptr = head
        for v in sorted(list2):
            ptr.val =v
            ptr = ptr.next

        return head

if __name__ == "__main__":
    s =Solution()
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n5 = ListNode(2)
    n6 = ListNode(8)

    n2.next = n3    
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = None

    res = s.sort(n2)
    while res:
        print(res.val, end= " ")
        res = res.next



