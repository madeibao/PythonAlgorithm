

# recently viewed file: tree/searchBST.py

# -*- coding: utf-8 -*-


# @Author: Mayuan
# @Time: 2026/10/1/星期四 15:45
# @File: searchBST
# @Description: 搜索二叉树中的值, 并返回该节点

from TreeNode import TreeNode

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().searchBST(root, 2))