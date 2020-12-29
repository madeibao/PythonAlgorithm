


class Solution:

	class TreeNode:
	    def __init__(self, x):
	        self.val = x
	        self.left = None
	        self.right = None

	def isUnivalTree(self, root: TreeNode) -> bool:
		self.val = None
		def check(root):
			if not root: return True
			if self.val is None: self.val = root.val
			return root.val==self.val and check(root.left) and check(root.right) 
		return check(root)

if __name__=='__main__':
	s = Solution()
	# 如何使用嵌套的内部类的结果值。
	root = s.TreeNode(1)
	l2 = s.TreeNode(1)
	l3 = s.TreeNode(1)

	root.left = l2
	root.right = l3

	print(s.isUnivalTree(root))

#======----------------------------------------------------------------
#------------------------------------------------------------------------------

# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	def isUnivalTree(self, root: TreeNode) -> bool:
		self.val = None
		def check(root):
			if not root: return True
			if self.val is None: self.val = root.val
			return root.val==self.val and check(root.left) and check(root.right) 
		return check(root)



if __name__=='__main__':
	s = Solution()

	# 如何使用嵌套的内部类的结果值。
	root = TreeNode(1)
	l2 = TreeNode(1)
	l3 = TreeNode(1)

	root.left = l2
	root.right = l3

	print(s.isUnivalTree(root))

