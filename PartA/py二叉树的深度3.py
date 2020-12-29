

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if root.left == None and root.right == None:
            return 1
        n1 = 0
        n2 = 0
        if root.left != None:
            n1 = self.maxDepth(root.left)
        if root.right != None:
            n2 = self.maxDepth(root.right)
        return max(n1, n2) + 1


if __name__ == "__main__":
    s = Solution()
    n2 = TreeNode(3)
    n3 = TreeNode(2)
    n4 = TreeNode(3)

    n2.left = n3
    n2.right = n4

    nm = TreeNode(3)
    nr = TreeNode(1)

    n3.right = nm
    n4.right = nr
print(s.maxDepth(n2))

