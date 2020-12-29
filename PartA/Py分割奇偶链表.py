
'''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/odd-even-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None 
'''
class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1 = head
        p2 = p3 = head.next
        while p1.next and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next

        p1.next = p3
        return head

if __name__ == '__main__':
	s = Solution()

	n2 = ListNode(2)
	n3 = ListNode(1)
	n4 = ListNode(3)
	n5 = ListNode(5)
	n6 = ListNode(6)
	n7 = ListNode(4)
	n8 = ListNode(7)


	n2.next = n3	
	n3.next = n4
	n4.next = n5 
	n5.next = n6
	n6.next = n7
	n7.next = n8
	n8.next = None

	res = s.oddEvenList(n2)

	while res:
		print(res.val,end=' ')
		res = res.next
