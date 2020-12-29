

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def invertTree(self, root):
		if not root:
			return root

		def dfs(root):
			if not root:
				return 
			root.left, root.right = root.right, root.left

			dfs(root.left)
			dfs(root.right)

		dfs(root)
		return root 






