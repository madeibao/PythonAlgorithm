

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def allpaths(self,root):
		if not root:
			return False

		if not root.left and not root.right:
			return [str(root.val)]

		left2 = self.allpaths(root.left)
		right2 = self.allpaths(root.right)

		alls = left2 +right2
		return [str(x)+"->" for x  in alls]


if __name__ == "__main__":
	s =Solution()

	n2 = TreeNode(1)
	n3 = TreeNode(2)
	n4 = TreeNode(3)

	n2.left =n3
	n2.right =n4
	print(s.allpaths(n2))
