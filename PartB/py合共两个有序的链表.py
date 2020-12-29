

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def compute(self,list2,list3):
        if list2==None:
            return list3
        
        if list3==None:
            return list2

        # 保存结果值。
        res = ListNode(-1)
        temp = res 

        h2 = list2
        h3 = list3


        while h2!=None and h3!=None:
            if h2.val<h3.val: 
                temp.next = h2
                h2 = h2.next
            else:
                temp.next = h3
                h3 = h3.next

            temp = temp.next

    
        if h2!=None:
            temp.next = h2
        
        if h3!=None:
            temp.next = h3

        return res.next


if __name__ == "__main__":
	s =Solution()

	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4) 

	n2.next = n3
	n3.next = n4
	n4.next = None

	h2 = ListNode(5)
	h3 = ListNode(6)
	h4 = ListNode(7)
	h2.next = h3
	h3.next = h4
	h4.next = None

	res = s.compute(n2, n3)

	while res:
		print(res.val,end=" ")
		res = res.next


