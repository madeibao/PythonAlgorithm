

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
        q = deque([root])
        level = 1
        ans = 1
        min_sum = float('inf')

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum < min_sum:
                min_sum = level_sum
                ans = level
            level += 1

        return ans

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(Solution().minimumLevel(root))



        