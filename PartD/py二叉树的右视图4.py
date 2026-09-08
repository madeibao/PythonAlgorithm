from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def rightSideView(self, root: Optional[TreeNode])-> List[int]:
        res = []
        if not root:  # 判空：空树直接返回空列表
            return res
        queue = deque()
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
    s = Solution()
    # 构造样例树
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(5)
    n5 = TreeNode(4)

    root.left = n2
    root.right = n3
    n2.right = n4
    n3.right = n5

    print(s.rightSideView(root))  # 输出 [1,3,4]
