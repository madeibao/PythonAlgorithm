

# 相同的二叉树和对称的二叉树的写法是一致的。
# 判断二叉树的写法。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return q.val ==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    s =Solution()
    n2 =TreeNode(2)
    n3 =TreeNode(3)
    n4 =TreeNode(4)

    n2.left =n3
    n2.right =n4

    h2 = TreeNode(2)
    h3 = TreeNode(3)
    h4 = TreeNode(4)

    h2.left =h3
    h2.right =h4

    print(s.isSameTree(n2,h2))

#--------------------------------------------------------------------------------------------------------------------
# 如果问题变成是否为对称的二叉树。
# 

class Solution(object):
    def symmetric(self, root):


        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return left.val==right.val and helper(left.left, right.right) and helper(left.right, right.left)
        
        if not root:
            return True
        
        return helper(root, root)

if __name__ == "__main__":
    s =Solution()
    n2 =TreeNode(2)
    n3 =TreeNode(3)
    n4 =TreeNode(3)

    n2.left =n3
    n2.right =n4

    print(s.symmetric(n2))






