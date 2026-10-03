# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/3/星期六 9:32
# @File: rightview
import collections
from typing import List
from typing import Optional
from TreeNode import TreeNode


class Solution(object):
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:  # 判空：空树直接返回空列表
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            n = len(queue)  # 当前这一层的节点总数
            for i in range(n):
                node = queue.popleft()
                # 当前层最后一个节点 → 右视图
                if i == n - 1:
                    res.append(node.val)
                # 先左后右入队，保证层级顺序
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(Solution().rightSideView(root))
