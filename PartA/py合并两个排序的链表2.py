
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def combine(self, list2, list3):

        if not list2:
            return list3
        if not list3:
            return list2

        a = list2
        b = list3

        temp = ListNode(-1)
        dump = temp

        while a!=None and b!=None:
            if a.val < b.val:
                dump.next = a
                a = a.next
            else:
                dump.next = b
                b = b.next
            dump = dump.next

        if a !=None:
            dump.next = a

        if b!=None:
            dump.next = b

        return temp.next


if __name__ == "__main__":
    s = Solution()

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

    res = s.combine(n2, h2)

    while res:
        print(res.val, end=" ")
        res = res.next



