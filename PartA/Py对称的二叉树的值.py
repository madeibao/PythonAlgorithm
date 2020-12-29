
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSameTree(p, q):
            if p == None and q == None:  
                return True
            if p and q and p.val == q.val:
                l = isSameTree(p.left, q.right) 
                r = isSameTree(p.right, q.left)
                return l and r 
            else:
                return False
        
        if root == None:
            return True
        else:
            return isSameTree(root.left, root.right)


if __name__ == "__main__": 
	s = Solution()
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(2)

	n1.left = n2
	n1.right = n3
	print(s.isSymmetric(n2))





	