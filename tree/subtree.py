# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 10:29
# @File: subtree.py
from typing import Optional
from tree import TreeNode

class Solution:
    def checkSubTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1:
            return False
        return (
                self.helper(t1, t2)
                or self.checkSubTree(t1.left, t2)
                or self.checkSubTree(t1.right, t2)
        )

    def helper(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (
                t1.val == t2.val
                and self.helper(t1.left, t2.left)
                and self.helper(t1.right, t2.right)
        )
