

from TreeNode import TreeNode
from collections import deque
from typing import Optional
from collections import defaultdict

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树中节点值之和最小的层号（层号从 1 开始）

        Args:
            root: 二叉树的根节点，可能为空

        Returns:
            节点值之和最小的层号；若树为空则返回 0
        """
        if not root:
            return 0
        q = deque([root])          # 层序遍历队列，初始只有根节点
        level = 1                  # 当前层号（从 1 开始）
        ans = 1                    # 记录最小层和的层号
        min_sum = float('inf')     # 记录目前的最小层和

        while q:
            level_sum = 0          # 当前层的节点值之和, 每次都要进行重置
            for _ in range(len(q)):  # 固定本轮处理节点数，即当前层全部节点
                node = q.popleft()
                level_sum += node.val
                if node.left:      # 左子节点入队，作为下一层节点
                    q.append(node.left)
                if node.right:     # 右子节点入队，作为下一层节点
                    q.append(node.right)

            if level_sum < min_sum:  # 严格小于，层和相同时保留更小的层号
                min_sum = level_sum
                ans = level
            level += 1             # 进入下一层
        return ans

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().minimumLevel(root))



        