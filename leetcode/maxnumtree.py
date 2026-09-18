# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 22:06
# @File: maxnumtree
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:

        dicta = {}
        deque = collections.deque([root])
        while deque:
            cur = deque.popleft()
            if cur.val not in dicta:
                dicta[cur.val] = 1
            else:
                dicta[cur.val] += 1

            if cur.left is not None:
                deque.append(cur.left)
            if cur.right is not None:
                deque.append(cur.right)

        maxval = max(dicta.values())
        res = []
        for item, val in dicta.items():
            if val >= maxval:
                res.append(item)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.findMode(root))