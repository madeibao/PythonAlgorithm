
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    print(s.maxDepth(TreeNode(3)))