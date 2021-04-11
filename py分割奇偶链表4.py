

# 分割奇数和偶数的链表值。
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
	def split(self,head):

		odd = head 
		even_head = even = head.next

		while odd.next and even.next:
			odd.next = odd.next.next
			even.next = even.next.next

			odd = odd.next
			even = even.next

		odd.next = even_head
		return head


if __name__ == "__main__":
    s = Solution()

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

    res = s.split(n2)

    while res:
        print(res.val,end="->")
        res =res.next
    
