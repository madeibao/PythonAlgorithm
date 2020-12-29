# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2019/10/31 18:31
# @File: Test.py


class ListNode:
    def __init__(self, x):
        self.elem = x
        self.next = None


    # 判断列表是否为空的列表。
    def is_empty(self):
        return self.__head == None

    # 返回列表的长度。
    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        print('[', end="")
        cur = self.__head
        # 定义当前的节点
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("]")

    def add(self, item):
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur != None:
                cur = cur.next
            cur.next = node

    # 插入一个节点。
    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > (self.length() - 1):
            self.append(item)
        else:
            node = ListNode(item)
            count = 0
            prev = self.__head
            while count < (index - 1):
                count += 1
                prev = prev.next
            node.next = prev.next
            prev.next = node

    def remove(self, item):
        cur = self.__head
        prev = None
        while cur != None:
            if cur.elem == item:
                if not prev:
                    self.__head = cur.next
                else:
                    prev.next = cur.next
                return
            else:
                prev = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    node = ListNode()
    print(node.travel())







