# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/20/星期日 17:44
# @File: completetree

from collections import deque
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        seen_null = False  # 是否已经遇到过空节点

        while queue:
            node = queue.popleft()

            if node is None:
                seen_null = True
            else:
                # 关键判断：空节点之后又出现了非空节点
                if seen_null:
                    return False
                # 左右孩子无论是否为空，都入队
                queue.append(node.left)
                queue.append(node.right)

        return True


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(Solution().isCompleteTree(root))
