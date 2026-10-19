


from TreeNode import TreeNode
from typing import Optional

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node: Optional[TreeNode], max_val: int) -> None:
            if not node:
                return
            if node.val >= max_val:
                self.ans += 1
                max_val = node.val
            
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, float('-inf'))
        return self.ans

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(1)
    print(Solution().goodNodes(root))

