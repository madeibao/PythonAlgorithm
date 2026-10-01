# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/1/星期四 21:32
# @File: leftbottomval.py
from TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        deque = [root]
        ans = 0
        while deque:
            size = len(deque)
            for i in range(size):
                node = deque.pop(0)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
                if i == 0:
                    ans = node.val
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().findBottomLeftValue(root))
