# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 9:16
# @File: levelorder
import collections

from TreeNode import TreeNode
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode | None) -> List[List[int]]:
        if not root:
            return []
        deque = collections.deque()
        deque.append(root)
        result = []
        while deque:
            level = []
            length = len(deque)
            for i in range(length):
                node = deque.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        deque.append(node.left)
                    if node.right:
                        deque.append(node.right)
            result.append(level)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    res = Solution().levelOrder(root)
    print(res)
