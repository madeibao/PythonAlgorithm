
# 合并两个有序的链表，

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def mergeTwoLists(self, l1, l2):

    	if l1==None:
    		return l2	
    	if l2==None:
    		return l1 	

    	dummy = ListNode(0)
    	temp = dummy
        
    	while l1!=None and l2!=None:
    		if l1.val<= l2.val:
    			temp.next = l1
    			l1 = l1.next
    			temp= temp.next
    		else:
    			temp.next =l2
    			l2 = l2.next 
    			temp= temp.next 

    	if l1==None:
    		temp.next = l2
    	if l2==None:
    		temp.next = l1

    	return dummy.next




if __name__ == '__main__':
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
    res = s.mergeTwoLists(n1, h1)
    while res:
        print(res.val, end="->")
        res = res.next

