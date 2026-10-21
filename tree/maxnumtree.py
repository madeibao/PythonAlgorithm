# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/9/18/星期五 22:06
# @File: maxnumtree
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _count_values(self, root: TreeNode | None) -> dict:
        """层序遍历二叉树，统计每个节点值出现的次数。

        :param root: 二叉树的根节点
        :return: 键为节点值、值为该值出现次数的字典
        """
        dicta = {}
        deque = collections.deque([root])
        while deque:
            cur = deque.popleft()
            if cur.val not in dicta:
                dicta[cur.val] = 1
            else:
                dicta[cur.val] += 1

            if cur.left is not None:
                deque.append(cur.left)
            if cur.right is not None:
                deque.append(cur.right)

        return dicta

    def _get_modes(self, dicta: dict) -> list[int]:
        """从出现次数统计结果中找出所有众数。

        :param dicta: 键为节点值、值为该值出现次数的字典
        :return: 出现次数等于最大出现次数的所有节点值组成的列表
        """
        maxval = max(dicta.values())
        res = []
        for item, val in dicta.items():
            if val >= maxval:
                res.append(item)
        return res

    def findMode(self, root: TreeNode | None) -> list[int]:
        """找出二叉树中出现次数最多的所有节点值。

        :param root: 二叉树的根节点
        :return: 所有出现次数最多的节点值组成的列表
        """
        dicta = self._count_values(root)
        return self._get_modes(dicta)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    s = Solution()
    print(s.findMode(root))