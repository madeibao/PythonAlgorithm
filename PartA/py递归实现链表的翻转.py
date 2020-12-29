


class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None



class Solution(object):
    def reverse(self,head):
        if head==None or head.next==None:
            return head

        ListNode tail = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return tail


if __name__=='__main__': 
    s= Solution()

    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(4)
    n7 = ListNode(5)

    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    res = s.reverse(head)
    while res:
        print(res.val,end='->')
        res = res.next #
        
