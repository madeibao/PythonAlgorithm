# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 21:30
# @File: counttree

from typing import Optional
from TreeNode import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        la = root
        lb = root
        ha = 0
        hb = 0
        while la:
            la = la.left
            ha += 1
        while lb:
            lb = lb.right
            hb += 1
        if ha == hb:
            return pow(2, ha) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().countNodes(root))
