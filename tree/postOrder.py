# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/31/星期六 16:32
# @File: postOrder.py

from TreeNode import TreeNode
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().postorderTraversal(root))
