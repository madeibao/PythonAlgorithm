
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        next_node = None

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


if __name__ == "__main__":

    ListNodea = ListNode(1)
    ListNodeb = ListNode(2)
    ListNodec = ListNode(3)
    ListNoded = ListNode(4)
    ListNodee = ListNode(5)
    ListNodef = ListNode(6)
    ListNodeg = ListNode(7)
    ListNodeh = ListNode(8)

    left = 3
    right = 6

    ListNodea.next = ListNodeb
    ListNodeb.next = ListNodec
    ListNodec.next = ListNoded
    ListNoded.next = ListNodee
    ListNodee.next = ListNodef
    ListNodef.next = ListNodeg
    ListNodeg.next = ListNodeh
    ListNodeh.next = None

    solution = Solution()
    reversed_head = solution.reverseBetween(ListNodea, left, right)

    # 打印反转后的链表
    current = reversed_head
    while current:
        print(current.val)
        current = current.next

    print("反转后的链表打印完毕")


