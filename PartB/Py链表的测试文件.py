
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def list2(self, head):
        prev = head
        count = 0
        while count < 4 and prev:
            count += 1
            prev = prev.next

        print(head.val)
        return count


if __name__ == "__main__":
    s = Solution()
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n7 = ListNode(7)

    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = None

    print(s.list2(n2))




