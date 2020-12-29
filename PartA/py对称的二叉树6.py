# 判断一个二叉树是否位对称的二叉树。

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def symmetric(self,root):

		def helper(left, right):
			if not left and not right:
				return True
			if not left or not right:
				return False

			return left.val ==right.val and helper(left.left, right.right) and helper(left.right, right.left)
		return helper(root.left, root.right)

if __name__ == "__main__":
	s =Solution()

	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(3)

	n2.left = n3
	n2.right = n4

	print(s.symmetric(n2))












