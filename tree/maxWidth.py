
from TreeNode import TreeNode
from typing import List
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        res = []
        q = deque([(root, 1)])
        maxWidth = 1
        while q:
            levelSize = len(q)
            ans = []
            for _ in range(levelSize):
                node, val = q.popleft()
                ans.append(val)
                if node.left:
                    q.append((node.left, val * 2))
                if node.right:
                    q.append((node.right, val * 2 + 1))
            maxWidth = max(maxWidth, ans[-1] - ans[0] + 1)
        return maxWidth

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = None
    root.left.right = None
    root.right.left = None
    root.right.right = None
    print(Solution().widthOfBinaryTree(root))

