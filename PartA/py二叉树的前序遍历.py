
from typing import List

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preOrder(self,root)->List[int]:
		res = []

		def dfs(root):
			# 调用外部的变量的值。
			nonlocal res
			if not root:
				return 
			res.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return res

if __name__ == "__main__": 
	s =Solution()

	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)

	n2.left = n3
	n2.right = n4

	print(s.preOrder(n2))

