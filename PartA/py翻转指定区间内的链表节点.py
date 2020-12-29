
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next =  head

        g = dummyHead
        p = dummyHead.next

        step =0
        while step<m-1:
            g= g.next
            p= p.next
            step+=1

        for i in range(n-m):
            remove = p.next
            p.next = remove.next
            remove.next = g.next 
            g.next = remove
        return dummyHead.next


if __name__ == "__main__":
    s =Solution()

    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = None

    res = s.reverseBetween(n2, 2, 4)
    while res:
        print(res.val, end=" ")
        res = res.next

        


