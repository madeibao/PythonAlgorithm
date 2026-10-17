

from TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val
        ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumOfLeftLeaves(root))