


# 求一个二叉树的最大的高度值。
# 最大的高度。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        if root.left==None and root.right == None:
            return 1
        n1=0
        n2=0
        if root.left!=None:
            n1 = self.maxDepth(root.left)
        if root.right!=None:
            n2 = self.maxDepth(root.right) 
        return max(n1,n2)+1


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left =n2
    n1.right =n3

    print(s.maxDepth(n1))
