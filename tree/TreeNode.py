# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/1/星期四 15:45
# @File: TreeNode

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root):
    if not root:
        return []
    q = deque([root])
    result = []
    while q:
        level_size = len(q)  # 当前层节点数量
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)  # level是本层新列表，存进去
    return result


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    print(traverse(tree))
