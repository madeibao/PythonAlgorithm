
from typing import List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + "->" + s for s in sub_paths]


if __name__ == "__main__":
    s = Solution()

    n2 = TreeNode(2)
    n3 = TreeNode(4)
    n4 = TreeNode(5)

    n5 = TreeNode(6)

    n2.left = n3
    n2.right = n4
    n3.left = n5

    res = s.binaryTreePaths(n2)

    print(res)

