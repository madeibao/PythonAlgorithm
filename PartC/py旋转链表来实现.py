
# 链表的旋转实现。
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# ============================ =================================
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        oldTail = head
        length = 1
        while oldTail.next:  # 计算长度
            length += 1
            oldTail = oldTail.next
        oldTail.next = head  # 闭环

        newTail = head
        number = k % length  # 求余数
        for _ in range(length - number - 1):  # 找到新的尾结点
            newTail = newTail.next
        newHead = newTail.next

        newTail.next = None  # 断链
        return newHead


if __name__ == "__main__":
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    res = s.rotateRight(n1, 2)
    while res:
        print(res.val, end="->")
        res = res.next





