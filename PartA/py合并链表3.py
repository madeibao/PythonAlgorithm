
# 递归的写法和终止条件。
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None 


class Solution(object):
    def combine(self,headA, headB):

    	# 递归必须有终止条件。
        if not headA:
            return headB    
        if not headB:
            return headA

        temp = None
        if headA.val <headB.val:
            temp = headA
            temp.next = self.combine(headA.next,headB)
        else:
            temp = headB    
            temp.next = self.combine(headA,headB.next)

        return temp


if __name__ == "__main__":
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    h1 = ListNode(2)
    h2 = ListNode(3)
    h3 = ListNode(4)
    h1.next= h2
    h2.next= h3
    h3.next= None
    s = Solution()
    res = s.combine(n1, h1)
    while res:
        print(res.val, end="->")
        res = res.next
