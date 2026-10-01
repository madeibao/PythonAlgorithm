# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/1/星期四 15:45
# @File: deletenode

from TreeNode import TreeNode
from typing import Optional
from TreeNode import traverse

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> TreeNode | None:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root

    def print_tree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        # 访问根节点
        print(root.val)
        # 递归打印左子树
        self.print_tree(root.left)
        # 递归打印右子树
        self.print_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(7)
    root.left.right.left.left = TreeNode(6)
    root.left.right.left.right = TreeNode(8)
    root.left.right.right.right = TreeNode(9)

    target = 3

    res = Solution().removeLeafNodes(root, target)
    print(traverse(res))
