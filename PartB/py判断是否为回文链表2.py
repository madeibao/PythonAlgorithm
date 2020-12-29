
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseNode(self, head):
        res = []

        while head:
            res.append(head.val)
            head = head.next

        return res == res[::-1]


if __name__ == "__main__":
    s = Solution()
    n2 = ListNode(1)
    n3 = ListNode(2)
    n4 = ListNode(1)

    n2.next = n3
    n3.next = n4
    n4.next = None

    print(s.reverseNode(n2))



