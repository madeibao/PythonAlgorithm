

from ListNode import ListNode

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """
        获取链表中指定索引位置的节点值

        Args:
            index: 要获取的节点索引，从 0 开始

        Returns:
            指定索引位置节点的 val 值；若索引越界则返回 -1
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next


if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # linked list becomes 1->2->3
    print(myLinkedList.get(1))     # return 2

