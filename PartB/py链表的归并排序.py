
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def sort(self,head):
        if not head or not head.next:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None    

        # 递归的分割下去。
        n2 = self.sort(head)
        n3 = self.sort(mid)

        n4 = self.merge(n2,n3)
        return n4

    def merge(self,headA, headB):
        if not headA:
            return headB
        if not headB:
            return headA 

        n3 = ListNode(-1)
        temp = n3

        A= headA
        B= headB

        while A and B:
            if A.val<B.val:
                temp.next = A
                A= A.next
            else:
                temp.next = B
                B = B.next
            temp = temp.next

        if A:
            temp.next = A 

        if B:
            temp.next = B

        return n3.next    



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



