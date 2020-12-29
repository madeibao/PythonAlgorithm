
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum = float("-inf")
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.sum = max(self.sum,max(l,0)+max(r,0)+node.val)
            return max(0,l,r) + node.val
        dfs(root)
        return self.sum



if __name__ == "__main__":
    s =Solution()
    root = TreeNode(2)
    l2 = TreeNode(1)
    r2 = TreeNode(3)

    root.left = l2
    root.right = r2

    print(s.maxPathSum(root))

    