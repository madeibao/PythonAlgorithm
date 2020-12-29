# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        # step1: push 
        curr = head
        while(curr):
            stack.append(curr)
            curr = curr.next
        # step2: pop and compare
        node1 = head
        while(stack):
            node2 = stack.pop()
            if node1.val != node2.val:
                return False
            node1 = node1.next
        return True


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    s = Solution()
    temp= s.isPalindrome(n1)
    print(temp)


