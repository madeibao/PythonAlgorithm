


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, low = float('-inf'), high = float('inf')) -> bool:
        if not root: return True
        if not low<root.val<high: return False
        return self.isValidBST(root.left,low,root.val) and self.isValidBST(root.right,root.val,high)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(2)
    l2 = TreeNode(1)
    l3 = TreeNode(3)

    root.left = l2
    root.right = l3

    print(s.isValidBST(root))




