
from TreeNode import TreeNode

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        def dfs(node: TreeNode | None, path_sum: int) -> int:
            if not node:
                return 0
            temp = 10 * path_sum + node.val
            if not node.left and not node.right:
                return temp
            return dfs(node.left, temp) + dfs(node.right, temp)
        
        return 0 if not root else dfs(root, 0)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root))

