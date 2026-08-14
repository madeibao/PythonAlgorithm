

from collections import deque
from typing import List, Optional

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """二叉树的层次遍历（BFS，借助队列，逐层收集节点值）"""
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res


def buildTree(values: List) -> Optional[TreeNode]:
    """根据层次遍历的数组（None 表示空节点）来构建二叉树"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()

    # 初始化数据：
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    values = [1, 2, 3, 4, 5, None, 6]
    root = buildTree(values)

    print("层次遍历结果:", s.levelOrder(root))
