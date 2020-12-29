
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None

        if not root.left and not root.right:
            return root

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def firstTree(root):
    if not root:
        return None

    print(root.val)
    firstTree(root.left)
    firstTree(root.right)


if __name__ == "__main__":
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(3)

    n2.left = n3
    n2.right = n4

    s = Solution()
    res = s.invertTree(n2)

    firstTree(res)


