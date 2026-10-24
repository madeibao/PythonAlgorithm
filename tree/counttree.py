# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 21:30
# @File: counttree
# @Description: 给定一棵完全二叉树，求这棵树的节点个数， 基本思路是递归， 但是题目要求时间复杂度为O(logN) ， 所以要用二分法来找规律。
# 首先是判断左子树的高度和右子树的高度， 如果相等， 那么说明是满二叉树， 直接用公式计算即可。 若不等， 则递归求解左右子树的节点个数之和加1.
# @Software: PyCharm 
# @Version: 1.0 

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
