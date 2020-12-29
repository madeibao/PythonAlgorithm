# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2020/6/9 9:21
# @File: Test.py

from typing import List
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res


if __name__ == "__main__":
    s = Solution()

    root = TreeNode(2)
    n2 = TreeNode(9)
    n3 = TreeNode(20)

    n4 = TreeNode(15)
    n5 = TreeNode(7)

    root.left = n2
    root.right = n3

    n3.left = n4
    n3.right = n5

    res = s.levelOrder(root)
    print(res)

