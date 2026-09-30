
from typing import Optional
from TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        cur = 0
        left = 0
        right = 0
        if root.left and root.left.left is None and root.left.right is None:
            cur = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        right += self.sumOfLeftLeaves(root.right)
        return cur +left+right

if __name__=="__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.left = b
    a.right = c
    print(Solution().sumOfLeftLeaves(a))


        

