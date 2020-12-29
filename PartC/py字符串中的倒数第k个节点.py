
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
head = Node(0)
temp = head
for i in range(1,8):
    node = Node(i)
    temp.next = node
    temp = node


# 指向第一个节点的位置上。
first = head.next
i = 0
k = int(input())
while i < k-1:
    first = first.next
    i += 1

print(i)
slow = head.next
while first.next:
    first = first.next
    slow = slow.next


# 返回比较慢的指针的节点的值。
print(slow.val)

