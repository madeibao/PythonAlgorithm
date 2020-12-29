
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newHead = ListNode()
        temp = newHead
        while (l1 and l2):
            if l1.val < l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return newHead.next


def createListNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


if __name__ == "__main__":
    s = Solution()
    head2 = createListNode([1, 2, 3, 4])
    head3 = createListNode([2, 3, 3])

    res = s.mergeTwoLists(head2, head3)

    while res:
        print(res.val, end='->')
        res = res.next


#----------------------------------------------------------------------- #
#递归的写法来实现合并两个有序的链表
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution(object):
    def combine(self,headA, headB):

        if not headA:
            return headB
        if not headB:
            return headA
        temp = None

        if headA.val<headB.val:
            temp = headA
            temp.next = self.combine(headA.next,headB)
        else:
            temp = headB
            temp.next = self.combine(headA, headB.next)

        return temp

def createListNode(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


if __name__ == "__main__":
    s = Solution()
    head2 = createListNode([1, 2, 3, 4])
    head3 = createListNode([2, 3, 3])

    res = s.combine(head2, head3)

    while res:
        print(res.val, end='->')
        res = res.next
