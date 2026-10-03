# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 10:10
# @File: balancetree.py
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().isBalanced(root))
