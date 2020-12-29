
# Definition for singly-linked list.



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 通过在规定的时间复杂度和空间复杂度的条件下来判断是否位回文链表。
class Solution():
	def isPalindrome(self,head)->bool:

		if head==None or head.next==None:
			return True

		dummy = ListNode(-1)
		dummy.next = head

		slow = dummy
		fast = dummy


		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next


		fast = slow.next
		slow.next = None
		slow = dummy.next


		# 然后将后半段的链表内容来进行逆置。
		pre = None
		while fast:
			temp = fast.next
			fast.next =pre
			pre = fast
			fast = temp

		while pre:
			if pre.val!= slow.val:
				return False
			pre = pre.next
			slow = slow.next 
		return True



if __name__ == "__main__": 
	s = Solution()
	n2 = ListNode(1)
	n3 = ListNode(2)
	n4 = ListNode(1)
	n2.next = n3	
	n3.next = n4
	n4.next = None


	print(s.isPalindrome(n2))
