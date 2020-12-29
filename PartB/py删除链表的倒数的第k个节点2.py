
class ListNode(object):
    def __init__(self,x):
        self.val = x 
        self.next = None #

class Solution(object):
    def reverseKthNode(self,head,k):

        if head==None:
            return None
        if k<=0:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(k):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next =  slow.next.next
        return dummy.next


if __name__=='__main__':
    s =Solution()
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    k = 2
    res = s.reverseKthNode(n2, k)
    while res:
        print(res.val,end="->")
        res= res.next



        